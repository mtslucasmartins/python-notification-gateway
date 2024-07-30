import logging, sys
from abc import ABC, abstractmethod
from threading import Thread
from confluent_kafka import Consumer, KafkaException
from settings import KAFKA_CONFIG
from app.queues.handlers import SmsMessageHandler

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BaseConsumer(ABC):

    def __init__(self, consumer_topic: str, consumer_conf: dict) -> None:
        self._consumer_topic = consumer_topic
        self._consumer_conf = consumer_conf
        self._running = False

    @abstractmethod    
    def consume(self) -> None:
        pass

    def poll(self, timeout=1.0) -> None:
        self._consumer.poll(timeout=timeout)

    def start(self) -> bool:
        logger.info("starting")
        if not self._running:
            self._running = True
            self._consumer = Consumer(self._consumer_conf)
            self._consumer.subscribe([self._consumer_topic])

            self.consumer_thread = Thread(target=self.consume)
            self.consumer_thread.daemon = True
            self.consumer_thread.start()
        return self._running

    def stop(self) -> bool:
        if self._running:
            self._running = False
            if self.consumer_thread.is_alive():
                self.consumer_thread.join()
            self._consumer.close()
        return not self._running


class SmsConsumer(BaseConsumer):

    def __init__(self, consumer_topic: str, consumer_conf: dict) -> None:
        super().__init__(consumer_topic, consumer_conf)
        self._handler = SmsMessageHandler()

    def consume(self) -> None:
        try:
            while self._running:
                message = self.poll()
                if message and message.error():
                    self._handler.handle_error(message)
                elif message:
                    self._handler.handle_message(message)
        except KafkaException as e:
            logger.error(f"KafkaException on consumer polling: {e}")
        finally:
            if self._consumer:
                self._consumer.close()


class ConsumerFactory:

    @classmethod
    def get_default_sms_consumer(cls) -> SmsConsumer:
        consumer_topic = "mts.notification.sms.outbound"
        consumer_conf = {
            "group.id": KAFKA_CONFIG['kafka.group.id'],
            "bootstrap.servers": KAFKA_CONFIG['kafka.bootstrap.servers'],
            "auto.offset.reset": KAFKA_CONFIG['kafka.auto.offset.reset'],
        }
        return SmsConsumer(consumer_topic, consumer_conf)

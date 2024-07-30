import logging
from abc import ABC, abstractmethod
from confluent_kafka import Producer, Message, KafkaError, KafkaException
from settings import KAFKA_CONFIG

logger = logging.getLogger(__name__)

class BaseProducer(ABC):

    def __init__(self, producer_topic: str, producer_conf: dict) -> None:
        self._producer_topic = producer_topic
        self._producer_conf = producer_conf
        self._producer = Producer(self._producer_conf)

    @abstractmethod
    def delivery_callback(self, error, message) -> None:
        pass

    def poll(self, seconds=1.0) -> None:
        self._producer.poll(seconds)

    def produce(self, serialized_message)-> None:
        self._producer.produce(
            self._producer_topic, 
            value=serialized_message, 
            callback=self.delivery_callback
        )


class SmsProducer(BaseProducer):

    def __init__(self, *args, **kwargs):
        self.outbound_topic = "mts.notification.sms.outbound"
        self.producer_conf = {
            "bootstrap.servers": KAFKA_CONFIG['kafka.bootstrap.servers'],
        }
        self.producer = Producer(self.producer_conf)

    def delivery_callback(self, error, message):
        if error is not None:
            logger.warn("delivery callback - message delivery failed")
        else:
            logger.info("delivery callback - message delivered")


class ProducerFactory:

    @staticmethod
    def get_default_sms_producer() -> SmsProducer:
        return SmsProducer()


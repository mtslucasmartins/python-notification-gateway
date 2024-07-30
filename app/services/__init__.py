from app.queues.consumers import ConsumerFactory
from app.queues.producers import ProducerFactory
from app.models.entities import Notification

class SmsService:

    __instance = None

    def __init__(self) -> None:
        self.__consumer = ConsumerFactory.get_default_sms_consumer()
        self.__producer = ProducerFactory.get_default_sms_producer()
    
    def consumer_start(self):
        self.__consumer.start()
    
    def consumer_stop(self):
        self.__consumer.stop()

    def producer_produce(self, message):
        self.__producer.produce(message)

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance
        return SmsService()

from app.queues.consumers import ConsumerFactory
from app.queues.producers import ProducerFactory

sms_consumer = ConsumerFactory.get_default_sms_consumer()
sms_producer = ProducerFactory.get_default_sms_producer()

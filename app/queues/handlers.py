from confluent_kafka import KafkaError, KafkaException

import logging, sys 

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class SmsMessageHandler:

    def __init__(self) -> None:
        pass

    def handle_error(self, message):
        """
        Method for handling error messages from a Kafka topic. 
        """
        message_error = message.error()
        message_topic = message.topic()
        message_partition = message.partition()
        message_offset = message.offset()
        if message_error.code() == KafkaError._PARTITION_EOF:
            logger.info(
                "%% %s [%d] reached end at offset %d\n", 
                message_topic, message_partition, message_offset
            )
        elif message_error:
            raise KafkaException(message_error) 

    def handle_message(self, message):
        """
        Method for handling Kafka messages.
        """
        message_topic = message.topic()
        message_partition = message.partition()
        logger.info(
            "%% [%s] [%d] handling message - message:[%s]", 
            message_topic, message_partition, message.value()
        )

import os 

# Twilio Required Variables.
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)

KAFKA_CONFIG = {
    "kafka.auto.offset.reset": os.environ.get("KAFKA_AUTO_OFFSET_RESET", 'smallest'),
    "kafka.bootstrap.servers": os.environ.get("KAFKA_BOOTSRAP_SERVERS", "192.168.49.2:30092"),
    "kafka.group.id":  os.environ.get("KAFKA_GROUP_ID", "test"),
}

TWILIO_CONFIG = {
    "twilio.account.sid": os.environ.get('TWILIO_ACCOUNT_SID', None),
    "twilio.auth.token": os.environ.get('TWILIO_AUTH_TOKEN', None)
}

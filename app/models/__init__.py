
class NotificationRequest:

    def __init__(self, **kwargs) -> None:
        self.notification_id = kwargs.get("notification_id")
        self.notification_method = kwargs.get("notification_method")
        self.notification_body = kwargs.get("notification_body")
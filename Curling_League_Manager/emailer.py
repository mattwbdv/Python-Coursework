class Emailer:
    _sole_instance = None
    sender_address = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def configure(cls, prop):
        cls.sender_address = prop

    # send_plain_email(recipients, subject, message) -- Note: this is an instance method.
    def send_plain_email(self, recipients, subject, message):
        for recipient in recipients:
            print(f"Sending mail to: " + recipient)


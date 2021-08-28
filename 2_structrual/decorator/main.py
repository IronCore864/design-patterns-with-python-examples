class Notifier():
    def notify(self):
        pass


class Decorator(Notifier):
    _notifier: Notifier = None

    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def operation(self):
        return self._notifier.notify()


class SMSDecorator(Decorator):
    def notify(self):
        return "SMS notification sent!"


class SlackDecorator(Decorator):
    def notify(self):
        return "Slack notification sent!"


def client_code(c: Notifier):
    print(c.notify())


if __name__ == "__main__":
    notifier = Notifier()
    sms = SMSDecorator(notifier)
    slack = SlackDecorator(notifier)
    client_code(sms)
    client_code(slack)

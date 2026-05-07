# Problem 5: Abstract Notification System

from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotifier(Notifier):

    def send_notification(self, message):
        print("Email sent:", message)


class SMSNotifier(Notifier):

    def send_notification(self, message):
        print("SMS sent:", message)


# Taking input from the user
message = input("Enter notification message: ")

notifiers = [EmailNotifier(), SMSNotifier()]

for n in notifiers:
    n.send_notification(message)
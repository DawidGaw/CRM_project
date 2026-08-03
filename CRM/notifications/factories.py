import factory
from clients.factories.client import ClientFactory
from factory.django import DjangoModelFactory
from notifications.models import Notification
from users.factories import UserFactory


class NotificationFactory(DjangoModelFactory):
    class Meta:
        model = Notification

    user = factory.SubFactory(UserFactory)
    client = factory.SubFactory(ClientFactory)
    key = factory.Sequence(lambda n: f"notification_{n}")
    message = factory.Faker("sentence")
    type = "followup"

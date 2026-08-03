from datetime import timedelta

import factory
from clients.factories.client import ClientFactory
from django.utils import timezone
from factory.django import DjangoModelFactory
from tasks.models import Task
from users.factories import UserFactory


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    user = factory.SubFactory(UserFactory)
    client = factory.SubFactory(ClientFactory)
    title = factory.Sequence(lambda n: f"Task #{n}")
    description = factory.Faker("paragraph")
    due_date = factory.LazyFunction(lambda: timezone.now() + timedelta(days=7))
    status = "todo"
    priority = "medium"
    reminder = factory.LazyAttribute(lambda obj: obj.due_date - timedelta(hours=1))

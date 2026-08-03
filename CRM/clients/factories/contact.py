import datetime

import factory
from clients.models import Contact
from factory.django import DjangoModelFactory
from users.factories import UserFactory

from .client import ClientFactory


class ContactFactory(DjangoModelFactory):
    class Meta:
        model = Contact

    client = factory.SubFactory(ClientFactory)
    user = factory.SubFactory(UserFactory)

    contact_type = "call"
    contact_date = factory.LazyFunction(datetime.date.today)
    note = factory.Faker("sentence")
    next_followup = None

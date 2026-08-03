import datetime
from decimal import Decimal

import factory
from clients.factories.client import ClientFactory
from deals.models import Deal
from factory.django import DjangoModelFactory
from users.factories import UserFactory


class DealFactory(DjangoModelFactory):
    class Meta:
        model = Deal

    title = factory.Sequence(lambda n: f"Deal {n}")
    client = factory.SubFactory(ClientFactory)
    owner = factory.SubFactory(UserFactory)

    value = Decimal("10000.00")
    stage = "lead"
    probability = 50

    expected_close_date = factory.LazyFunction(
        lambda: datetime.date.today() + datetime.timedelta(days=30)
    )

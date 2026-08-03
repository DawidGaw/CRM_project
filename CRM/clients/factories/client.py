from typing import Any

import factory
from clients.models import Client
from factory.django import DjangoModelFactory
from users.factories import UserFactory

from .tag import TagFactory


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client
        django_get_or_create = ("email",)

    company_name = factory.Sequence(lambda n: f"Company {n}")
    address = factory.Faker("address")
    email = factory.Sequence(lambda n: f"client{n}@example.com")
    phone_number = factory.Faker("phone_number")
    tax_number = factory.Sequence(lambda n: f"TAX{n:06d}")
    owner = factory.SubFactory(UserFactory)
    status = "lead"

    @factory.post_generation
    def tags(self, create: bool, extracted: list[Any] | None, **kwargs: Any) -> None:
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)
        else:
            self.tags.add(*TagFactory.create_batch(2))

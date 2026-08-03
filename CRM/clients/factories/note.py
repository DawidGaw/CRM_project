from typing import Any

import factory
from clients.models import ClientNote
from factory.django import DjangoModelFactory
from users.factories import UserFactory

from .client import ClientFactory
from .tag import TagFactory


class ClientNoteFactory(DjangoModelFactory):
    class Meta:
        model = ClientNote

    client = factory.SubFactory(ClientFactory)
    user = factory.SubFactory(UserFactory)
    content = factory.Faker("paragraph")

    @factory.post_generation
    def tags(self, create: bool, extracted: list[Any] | None, **kwargs: Any) -> None:
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)
        else:
            self.tags.add(*TagFactory.create_batch(2))

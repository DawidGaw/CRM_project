import factory
from clients.models import Tag
from factory.django import DjangoModelFactory


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = ("name",)

    name = factory.Sequence(lambda n: f"tag-{n}")

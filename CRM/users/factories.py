import factory
from factory.django import DjangoModelFactory
from users.models import User, UserSettings


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("email",)

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    role = "sales"
    is_active = True

    password = factory.PostGenerationMethodCall("set_password", "defaultpass123")


class UserSettingsFactory(DjangoModelFactory):
    class Meta:
        model = UserSettings

    user = factory.SubFactory(UserFactory)
    no_contact_days = 7
    followup_days = 2

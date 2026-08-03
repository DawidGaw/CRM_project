from django.test import TestCase
from users.factories import UserFactory, UserSettingsFactory
from users.models import User, UserSettings


class UserFactoryTestCase(TestCase):
    def test_create_saves_user_to_database(self) -> None:
        user = UserFactory()

        self.assertIsNotNone(user.pk)
        self.assertTrue(User.objects.filter(pk=user.pk).exists())

    def test_create_batch_creates_correct_number_of_users(self) -> None:
        users = UserFactory.create_batch(5)

        self.assertEqual(len(users), 5)
        self.assertEqual(User.objects.count(), 5)


class UserSettingsFactorySingleTestCase(TestCase):
    def test_create_saves_to_database(self) -> None:
        user_settings = UserSettingsFactory()

        self.assertIsNotNone(user_settings.pk)
        self.assertTrue(UserSettings.objects.filter(pk=user_settings.pk).exists())

    def test_create_batch_creates_correct_number(self) -> None:
        settings_list = UserSettingsFactory.create_batch(4)

        self.assertEqual(len(settings_list), 4)
        self.assertEqual(UserSettings.objects.count(), 4)

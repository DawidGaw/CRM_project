from django.test import TestCase
from notifications.factories import NotificationFactory
from notifications.models import Notification


class NotificationFactoryTestCase(TestCase):
    def test_create_saves_notification_to_database(self) -> None:
        notification = NotificationFactory()

        self.assertIsNotNone(notification.pk)
        self.assertTrue(Notification.objects.filter(pk=notification.pk).exists())

    def test_create_batch_creates_correct_number_of_notifications(self) -> None:
        notifications = NotificationFactory.create_batch(5)

        self.assertEqual(len(notifications), 5)
        self.assertEqual(Notification.objects.count(), 5)

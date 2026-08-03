from clients.factories.client import ClientFactory
from clients.factories.tag import TagFactory
from clients.models import Client
from django.test import TestCase


class ClientFactoryTestCase(TestCase):
    def test_create_saves_client_to_database(self) -> None:
        client = ClientFactory()

        self.assertIsNotNone(client.pk)
        self.assertTrue(Client.objects.filter(pk=client.pk).exists())

    def test_create_batch_creates_correct_number_of_clients(self) -> None:
        clients = ClientFactory.create_batch(5)

        self.assertEqual(len(clients), 5)
        self.assertEqual(Client.objects.count(), 5)

    def test_create_adds_default_tags(self) -> None:
        client = ClientFactory()

        self.assertEqual(client.tags.count(), 2)

    def test_create_uses_provided_tags(self) -> None:
        tag1 = TagFactory(name="VIP")
        tag2 = TagFactory(name="Startup")

        client = ClientFactory(tags=[tag1, tag2])

        self.assertEqual(client.tags.count(), 2)
        self.assertSetEqual(set(client.tags.all()), {tag1, tag2})

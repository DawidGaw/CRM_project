from clients.factories.note import ClientNoteFactory
from clients.factories.tag import TagFactory
from clients.models import ClientNote
from django.test import TestCase


class ClientNoteFactoryTestCase(TestCase):
    def test_create_saves_client_note_to_database(self) -> None:
        client_note = ClientNoteFactory()

        self.assertIsNotNone(client_note.pk)
        self.assertTrue(ClientNote.objects.filter(pk=client_note.pk).exists())

    def test_default_tags_are_created(self) -> None:
        client_note = ClientNoteFactory()

        self.assertEqual(client_note.tags.count(), 2)

    def test_custom_tags_are_used(self) -> None:
        tag1 = TagFactory(name="VIP")
        tag2 = TagFactory(name="Important")

        client_note = ClientNoteFactory(tags=[tag1, tag2])

        self.assertEqual(client_note.tags.count(), 2)
        self.assertSetEqual(set(client_note.tags.all()), {tag1, tag2})

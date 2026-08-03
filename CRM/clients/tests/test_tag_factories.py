from clients.factories.tag import TagFactory
from clients.models import Tag
from django.test import TestCase


class TagFactoryTestCase(TestCase):
    def test_create_saves_tag_to_database(self) -> None:
        tag = TagFactory()

        self.assertIsNotNone(tag.pk)
        self.assertTrue(Tag.objects.filter(pk=tag.pk).exists())

    def test_create_batch_creates_correct_number_of_tags(self) -> None:
        tags = TagFactory.create_batch(5)

        self.assertEqual(len(tags), 5)
        self.assertEqual(Tag.objects.count(), 5)

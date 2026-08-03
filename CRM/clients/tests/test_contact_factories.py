from clients.factories.contact import ContactFactory
from clients.models import Contact
from django.test import TestCase


class ContactFactoryTestCase(TestCase):
    def test_create_saves_contact_to_database(self) -> None:
        contact = ContactFactory()

        self.assertIsNotNone(contact.pk)
        self.assertTrue(Contact.objects.filter(pk=contact.pk).exists())

    def test_create_batch_creates_correct_number_of_contacts(self) -> None:
        contacts = ContactFactory.create_batch(5)

        self.assertEqual(len(contacts), 5)
        self.assertEqual(Contact.objects.count(), 5)

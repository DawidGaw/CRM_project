from deals.factories import DealFactory
from deals.models import Deal
from django.test import TestCase


class DealFactoryTestCase(TestCase):
    def test_create_saves_deal_to_database(self) -> None:
        deal = DealFactory()

        self.assertIsNotNone(deal.pk)
        self.assertTrue(Deal.objects.filter(pk=deal.pk).exists())

    def test_create_batch_creates_correct_number_of_deals(self) -> None:
        deals = DealFactory.create_batch(5)

        self.assertEqual(len(deals), 5)
        self.assertEqual(Deal.objects.count(), 5)

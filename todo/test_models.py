from django.test import TestCase
from .models import Item


# Test that our todo items are created with a default done value of False

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')


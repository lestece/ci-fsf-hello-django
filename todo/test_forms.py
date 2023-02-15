from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    # test that a name field is required in order to create an item
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # test that the done checkbox is not required in order to create an item/the form to be valid
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test todo item'})
        self.assertTrue(form.is_valid())

    # test that the only fields displayed in the form are the name and done fields
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])



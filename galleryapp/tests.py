from django.test import TestCase
from . models import Location,Category,Image

# Create your tests here.
class TestLocation(TestCase):

    def setUp(self):
        self.Ian = Location(location = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Ian,Location))

    # Testing Save Method
    def test_save_method(self):
        self.Ian.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

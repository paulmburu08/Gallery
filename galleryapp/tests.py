from django.test import TestCase
from . models import Location,Category,Image

# Create your tests here.
class TestLocation(TestCase):

    def setUp(self):
        self.Ian = Location(location = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Ian,Location))

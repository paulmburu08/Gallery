from django.test import TestCase
from . models import Location,Category,Image

# Create your tests here.
class TestLocation(TestCase):

    def setUp(self):
        self.location = Location(location = 'Nairobi')

    def tearDown(self):
        Location.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # Testing delete Method
    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    # Testing update Method
    def test_update_method(self):
        self.location.save_location()
        self.location.update_location(self.location.id,'Mombasa')
        locations = Location.objects.all()
        self.assertTrue(locations[0].location == 'Mombasa')


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category(category = 'Art')

    def tearDown(self):
        Category.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    # Testing delete Method
    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) == 0)

    # Testing update Method
    def test_update_method(self):
        self.category.save_category()
        self.category.update_category(self.category.id,'Travel')
        categorys = Category.objects.all()
        self.assertTrue(categorys[0].category == 'Travel')

class TestImage(TestCase):

    def setUp(self):
        self.wildlife = Category(category = 'wildlife')
        self.kenya = Location(category = 'kenya')
        self.image = Image(image = 'image1.png',name = 'An image',description = 'An image of Paul',upload_date = '2020-06-30 01:02:49.06078',location = 'self.kenya',category = 'self.wildlife')

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # Testing Save Method
    def test_save_method(self):
        self.kenya.save_location()
        self.wildlife.save_category()
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing delete Method
    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    # Testing update Method
    def test_update_method(self):
        self.image.save_image()
        self.image.update_image(self.image.id,'Image2.png')
        images = Image.objects.all()
        self.assertTrue(images[0].image == 'Image2.png')
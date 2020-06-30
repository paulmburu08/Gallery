from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,location):
        cls.objects.filter(id = id).update(location = location)

class Category(models.Model):
    category =  models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,category):
        cls.objects.filter(id = id).update(category = category)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.get(id = id)
        return images

    @classmethod
    def update_image(cls,id,image):
        cls.objects.filter(id = id).update(image = image)

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category__icontains=search_term)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__location__icontains = location)
        return images




from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)

class Category(models.Model):
    category =  models.CharField(max_length=30)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

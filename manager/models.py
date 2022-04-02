from distutils.command.upload import upload
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=300)
    description = RichTextUploadingField(null = True, blank = True)
    image = models.ImageField(upload_to = "services/", null = True, blank = True)

    objects = models.Manager()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = RichTextUploadingField(null = True, blank = True)
    image = models.ImageField(upload_to = "product/", null = True, blank = True)
    link = models.URLField(null = True, blank= True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=300)
    description = RichTextUploadingField(null = True, blank = True)
    image = models.ImageField(upload_to = "services/", null = True, blank = True)
    link = models.URLField(null = True, blank= True)
    
    objects = models.Manager()

    def __str__(self):
        return self.name

class Testomonial(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length = 300, null = True, blank = True)

    objects = models.Manager()

    def __str__(self):
        return self.name
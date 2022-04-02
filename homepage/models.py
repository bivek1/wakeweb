
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class CompanyInformation(models.Model):
    name = models.CharField(max_length=200, unique= True)
    short = models.CharField(max_length=300, unique= True)
    aims = RichTextUploadingField()
    logo = models.ImageField(upload_to = "logo/")
    objects = models.Manager()

    def __str__(self):
        return self.name


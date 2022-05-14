
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

class Worker(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Proff(models.Model):
    worker = models.ForeignKey(Worker, related_name="workerP", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = "work/")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.worker.name


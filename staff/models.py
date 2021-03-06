from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length= 200)
    objects = models.Manager()

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.PROTECT)
    name = models.CharField(max_length=300)

    objects = models.Manager()

    def  __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="blogs/", null = True, blank = True),
    category = models.ForeignKey(Category, related_name  = "blog_category", on_delete = models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, related_name = "blog_sub_category", on_delete= models.PROTECT, null = True, blank = True)
    description = RichTextUploadingField()
    visit = models.IntegerField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    objects = models.Manager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    
    blog = models.ForeignKey(Blog, related_name="blog_comment", on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.comment

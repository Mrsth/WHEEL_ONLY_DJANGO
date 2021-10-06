from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blogModel(models.Model):
    blogTitle = models.CharField(max_length=500)
    blogContent = RichTextField()
    blogOwner = models.CharField(max_length=100)
    blogLink = models.CharField(max_length=500, null=True, blank=True)
    blogImage = models.ImageField(upload_to='blogImages')

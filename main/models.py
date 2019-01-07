from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField


class ImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True, validators=[FileExtensionValidator(['jpg', 'png'])])
    title = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = RichTextField()
    created_time = models.DateTimeField()
    author = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(ImageModel, blank=True)

    def __str__(self):
        return self.title

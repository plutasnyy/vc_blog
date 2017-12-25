from django.db import models

class ImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null=True)
    title = models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(ImageModel)

    def __str__(self):
        return self.title



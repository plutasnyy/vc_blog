from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(blank=True, upload_to='files/blog/')
    title = models.CharField(max_length=60)
    short_des = models.CharField(max_length=155, blank=True)
    genre = models.ForeignKey(Genre, on_delete=None, blank=True)
    long_des = models.TextField(max_length=63300)
    writer = models.ForeignKey(User, on_delete=None)
    likes = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    comment = models.TextField(max_length=155)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

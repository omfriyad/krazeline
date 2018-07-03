from django.db import models
from django.utils import timezone

# Create your models here.


class Makeup(models.Model):
    title = models.CharField(max_length=256)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    image = models.ImageField()
    youtube_link = models.URLField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


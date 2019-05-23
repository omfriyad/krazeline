from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='files/profile_pics',blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

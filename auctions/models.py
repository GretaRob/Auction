from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listings(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField()
    price = models.FloatField()

    def __str__(self):
        return str(self.name)

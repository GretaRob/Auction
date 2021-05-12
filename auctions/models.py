from django.contrib.auth.models import AbstractUser
from django.db import models

CHOICES = (
    ('fasion', 'Fashion'),
    ('toys', 'Toys'),
    ('electronics', 'Electronics'),
    ('home', 'Home'),
    ('other', 'Other')
)


class User(AbstractUser):
    pass


class Listing(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.URLField(null=True, blank=True)
    price = models.FloatField()
    category = models.CharField(
        max_length=25, choices=CHOICES, default='Other')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

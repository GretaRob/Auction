from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE

CHOICES = (
    ('fashion', 'Fashion'),
    ('toys', 'Toys'),
    ('electronics', 'Electronics'),
    ('home', 'Home'),
    ('other', 'Other')
)


class User(AbstractUser):
    pass


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return str(self.price)


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_coms")
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.listing)

# parent model


class Listing(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.URLField(null=True, blank=True)
    price = models.FloatField()
    category = models.CharField(
        max_length=25, choices=CHOICES, default='Other')
    date_added = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=True)
    closed = models.BooleanField(default=False)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creators')
    bids = models.ManyToManyField(Bid, blank=True, related_name='bids')
    comments = models.ManyToManyField(
        Comment, blank=True, related_name="comments")

    def __str__(self):
        return str(self.name)


class Watchlist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='watchlist')
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='listings')

    def __str__(self):
        return f"{self.user.username} listed {self.listing.id}"

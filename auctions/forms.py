from django.forms import ModelForm
from django import forms
from datetime import date
from .models import Listing, Comment, Bid


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'image', 'price', 'category', 'description']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['price']

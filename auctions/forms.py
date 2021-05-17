from django.forms import ModelForm
from django import forms
from datetime import date
from .models import Listing, Comment, Bid


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'image', 'price', 'category']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'

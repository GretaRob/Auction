from django.forms import ModelForm
from django import forms
from datetime import date
from .models import Listing, Comment


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'image', 'price', 'category']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

from django.forms import ModelForm
from django import forms
from datetime import date
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'

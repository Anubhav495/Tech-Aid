from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import customuser

class customForm(ModelForm):
    class Meta:
        model = customuser
        fields = (
            'username',
            'email',
            'pass1',
            'pass2'
        )
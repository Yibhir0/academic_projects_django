from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# from ..item_app.models import Project
from .models import Project


class UpdateLikesForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['id', 'name', 'likes']

class UpdateRatingForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['id', 'name', 'avg_rating']
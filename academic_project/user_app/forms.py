from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Member


class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].help_text = "8+ Characters long"


class MemberFileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['profile_picture']
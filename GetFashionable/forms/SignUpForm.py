from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class SignUpForm(UserCreationForm):
    user_image = forms.ImageField(required=True, help_text='Upload your profile photo')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
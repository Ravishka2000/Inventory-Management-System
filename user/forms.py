from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    # define form look
    class Meta:
        # Model that used to create form
        model = User
        # set fields of the form
        fields = ['username', 'email', 'password1', 'password2']

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Member
from django import forms


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

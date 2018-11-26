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


class MemberCreateForm(forms.ModelForm):
    address_ = forms.CharField(max_length=50, label='Adres', required=False)
    zip_code = forms.CharField(max_length=10,  label='Kod pocztowy', required=False)
    city = forms.CharField(max_length=40, label='Miasto', required=False)

    class Meta:
        model = Member
        fields = [
            'name',
            'last_name',
            'address_',
            'zip_code',
            'city',
            'birth_date',
            'death_date',
            'dead',
            'phone_number']




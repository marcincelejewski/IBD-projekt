from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm, CustomUserChangeForm
from .models import Address
from .models import CustomUser
from .models import Family
from .models import Member


class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Family)
admin.site.register(Member)
admin.site.register(Address)

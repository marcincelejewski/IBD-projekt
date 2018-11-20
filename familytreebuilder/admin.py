from django.contrib import admin
from .models import User
from .models import Family
from .models import Member
from .models import Address
# Register your models here.

admin.site.register(User)
admin.site.register(Family)
admin.site.register(Member)
admin.site.register(Address)

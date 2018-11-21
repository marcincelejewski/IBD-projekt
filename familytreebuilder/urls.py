from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import Signup

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='familytreebuilder/home.html'), name='home'),
]


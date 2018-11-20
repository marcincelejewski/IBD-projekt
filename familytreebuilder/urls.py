from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignupCreateView.as_view(), name='signup'),

]


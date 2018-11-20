from django.shortcuts import render
from django.views.generic import CreateView
from . import models
# Create your views here.


def home(request):
    return render(request, 'familytreebuilder/home.html', {})


class SignupCreateView(CreateView):
    model = models.User
    fields = ['login', 'password']
    template_name = 'familytreebuilder/signup.html'




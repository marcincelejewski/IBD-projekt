from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


# Create your views here.


class Signup(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'familytreebuilder/signup.html'


def signup(request):
    if request.methid == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})





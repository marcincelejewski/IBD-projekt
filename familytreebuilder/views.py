from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .forms import SignUpForm, ImageUploadForm
from .models import Family
from .models import Member


# Create your views here.

class Signup(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'familytreebuilder/signup.html'


class MemberListView(ListView):
    model = Member


def home(request):
    if request.user.is_authenticated:
        family_list = get_list_or_404(Family, user__username=request.user.username)
        num_family = len(family_list)
        context = {
            'num_family': num_family,
            'family_list': family_list,
        }
        return render(request, 'familytreebuilder/home.html', context=context)
    else:
        return render(request, 'familytreebuilder/home.html')


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Family.objects.get(pk=request.family_id)
            m.photo = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

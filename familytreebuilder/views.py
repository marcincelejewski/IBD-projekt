from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Family, Member


# Create your views here.

class Signup(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'familytreebuilder/signup.html'


class FamilyListView(ListView):
    model = Family
    paginate_by = 10
    template_name = 'familytreebuilder/home.html'
    context_object_name = 'family_list'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(FamilyListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return get_list_or_404(Family, user__username=self.request.user.username)


class MemberListView(ListView):
    model = Member
    paginate_by = 50
    template_name = 'familytreebuilder/family.html'
    context_object_name = 'member_list'

    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        self.queryset = get_list_or_404(Member, family__pk=pk)
        return super(MemberListView, self).get(self, request, *args, **kwargs)


class MemberEditView(UpdateView):
    model = Member
    success_url = reverse_lazy('family')
    fields = ['name', 'last_name', 'address', 'death_date', 'birth_date', 'alive', 'phone_number']
    template_name = 'familytreebuilder/memberedit.html'

    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        self.queryset = get_object_or_404(Member, pk=pk)
        return super(MemberEditView, self).post(self, request, *args, **kwargs)






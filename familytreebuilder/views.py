from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import UpdateView

from .forms import SignUpForm, MemberCreateForm
from .models import Family, Member, Address


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

    def get_queryset(self):
        return Family.objects.filter(user__username=self.request.user.username)


class FamilyCreateView(CreateView):
    fields = ['name', 'photo']
    model = Family
    success_url = reverse_lazy('home')
    template_name = 'familytreebuilder/family_create.html'

    def form_valid(self, form):
        family = form.save(commit=False)
        family.user = self.request.user
        family.photo = form.cleaned_data['photo']
        family.save()
        return super(FamilyCreateView, self).form_valid(form)


class MakeRelationView(TemplateView):

    def get(self, request, *args, **kwargs):
        member = Member.objects.get(pk=kwargs['member_pk'])
        member_dest = Member.objects.get(pk=kwargs['member_dest_pk'])

        if kwargs['closest'] == 'parents':
            member.parents.add(member_dest)
        elif kwargs['closest'] == 'spouses':
            member.spouses.add(member_dest)
        elif kwargs['closest'] == 'children':
            member_dest.parents.add(member)

        url = reverse('family_show', kwargs={'family_pk': member.family.pk})
        return HttpResponseRedirect(url)


class MemberListView(ListView):
    model = Member
    paginate_by = 50
    template_name = 'familytreebuilder/family.html'
    context_object_name = 'member_list'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(MemberListView, self).post(self, request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(family__pk=self.kwargs['family_pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['family_pk'] = self.kwargs['family_pk']
        return context


class CreateRelationListView(ListView):
    model = Member
    paginate_by = 50
    template_name = 'familytreebuilder/create_relation.html'
    context_object_name = 'member_list'

    def get_queryset(self):
        member = get_object_or_404(Member, pk=self.kwargs['member_pk'])
        return super().get_queryset().filter(family=member.family)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['closest'] = self.kwargs['closest']
        context['member_pk'] = self.kwargs['member_pk']
        return context


class ClosestFamilyListView(ListView):
    model = Member
    paginate_by = 50
    template_name = 'familytreebuilder/closest_family.html'
    context_object_name = 'member_list'

    def get_queryset(self):
        # parrent

        if self.kwargs['closest'] == 'parents':
            return super().get_queryset().get(pk=self.kwargs['member_pk']).parents.all()
        # spouse
        elif self.kwargs['closest'] == 'spouses':
            return super().get_queryset().get(pk=self.kwargs['member_pk']).spouses.all()
        # dzieci
        elif self.kwargs['closest'] == 'children':
            return super().get_queryset().get(pk=self.kwargs['member_pk']).children.all()
        return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['closest'] = self.kwargs['closest']
        context['member_pk'] = self.kwargs['member_pk']
        return context


class MemberEditView(UpdateView):
    form_class = MemberCreateForm
    template_name = 'familytreebuilder/member_edit.html'

    def get_queryset(self):
        return Member.objects.filter(pk=self.kwargs['pk'])

    def get_initial(self):
        initial = super(MemberEditView, self).get_initial()
        member = get_object_or_404(Member, pk=self.kwargs['pk'])
        print(member)
        initial['address_'] = member.address.address
        initial['zip_code'] = member.address.zip_code
        initial['city'] = member.address.city
        return initial

    def form_valid(self, form):
        member = form.save(commit=False)
        member.save()

        address = form.cleaned_data['address_']
        zip_code = form.cleaned_data['zip_code']
        city = form.cleaned_data['city']

        Address.objects.filter(pk=member.address.pk).update(address=address, zip_code=zip_code, city=city)

        return super(MemberEditView, self).form_valid(form)

    def get_success_url(self):
        member = get_object_or_404(Member, pk=self.kwargs['pk'])
        return reverse_lazy('family_show', kwargs={'family_pk': member.family.pk})


class MemberCreateView(CreateView):
    form_class = MemberCreateForm
    template_name = 'familytreebuilder/member_create.html'

    def form_valid(self, form):
        member = form.save(commit=False)

        address = form.cleaned_data['address_']
        zip_code = form.cleaned_data['zip_code']
        city = form.cleaned_data['city']

        member.address = Address.objects.create(address=address, zip_code=zip_code, city=city)
        member_arg = None

        if self.kwargs['closest'] == 'parents':
            member_arg = Member.objects.get(pk=self.kwargs['member_pk'])
            family = member_arg.family
            member.generation = member_arg.generation + 1
        elif self.kwargs['closest'] == 'spouses':
            member_arg = Member.objects.get(pk=self.kwargs['member_pk'])
            family = member_arg.family
            member.generation = member_arg.generation
        elif self.kwargs['closest'] == 'children':
            member_arg = Member.objects.get(pk=self.kwargs['member_pk'])
            family = member_arg.family
            member.generation = member_arg.generation - 1
        # tworzymy pierwszego członka rodziny
        else:
            family = Family.objects.get(pk=self.kwargs['member_pk'])

        member.family = family
        family.inc_size()
        member.save()

        print(type(member))

        if self.kwargs['closest'] == 'parents':
            member_arg.parents.add(member)
        elif self.kwargs['closest'] == 'spouses':
            member.spouses.add(member_arg)
        elif self.kwargs['closest'] == 'children':
            member.parents.add(member_arg)

        return super(MemberCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.kwargs['closest'] == 'new':
            family_pk = self.kwargs['member_pk']
        else:
            member = get_object_or_404(Member, pk=self.kwargs['member_pk'])
            family_pk = member.family.pk
        return reverse_lazy('family_show', kwargs={'family_pk': family_pk})

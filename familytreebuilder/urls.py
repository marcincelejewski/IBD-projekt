from django.conf.urls import url
from django.urls import path, include

from .views import Signup, FamilyListView, MemberListView, MemberEditView, MemberCreateView, FamilyCreateView, \
    ClosestFamilyListView, CreateRelationListView, MakeRelationView

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', FamilyListView.as_view(), name='home'),
    path('family/<int:family_pk>/', MemberListView.as_view(), name='family_show'),
    path('member/<int:pk>/', MemberEditView.as_view(), name='member_edit'),
    path('family/create/', FamilyCreateView.as_view(), name='family_create'),
    url(r'^member/create/(?P<member_pk>(\d+))/(?P<closest>(\w+))/$', MemberCreateView.as_view(),
        name='member_create'),
    url(r'^family/closest/(?P<closest>(\w+))/(?P<member_pk>(\d+))/$', ClosestFamilyListView.as_view(),
        name='closest_family'),
    url(r'^family/create/relation/(?P<member_pk>(\d+))/(?P<closest>(\w+))/$', CreateRelationListView.as_view(),
        name='create_relation'),
    url(r'^family/make/relation/(?P<member_pk>(\d+))/(?P<member_dest_pk>(\d+))/(?P<closest>(\w+))/$',
        MakeRelationView.as_view(),name='make_relation')
]

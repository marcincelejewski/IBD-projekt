from django.urls import path, include
from .views import Signup, FamilyListView, MemberListView, MemberEditView, MemberCreateView, FamilyCreateView


urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', FamilyListView.as_view(), name='home'),
    path('family/<int:family_pk>/', MemberListView.as_view(), name='family_show'),
    path('member/<int:pk>/', MemberEditView.as_view(), name='member_edit'),
    path('member/create/<int:family_pk>/', MemberCreateView.as_view(), name='member_create'),
    path('family/create/', FamilyCreateView.as_view(), name='family_create'),

]


from django.urls import path, include
from .views import Signup, FamilyListView, MemberListView, MemberEditView


urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', FamilyListView.as_view(), name='home'),
    path('family/<int:pk>/', MemberListView.as_view(), name='show_family'),
    path('member/<int:pk>/', MemberEditView.as_view(), name='member'),

]


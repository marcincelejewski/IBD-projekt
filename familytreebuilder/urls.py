from django.urls import path, include
from .views import Signup
from .views import home
from .views import ImageUploadForm

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    #path('', ImageUploadForm, name='home')

]


from django.urls import path
from menu.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('accounts/registration/', RegistrationView.as_view(), name='registration'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]
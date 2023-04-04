from django.urls import path
from menu.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('accounts/login/', login_view, name='login'),
]
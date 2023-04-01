from django.shortcuts import render
from django.views.generic import ListView
from menu.models import MenuItem

# Create your views here.

class MenuView(ListView):
    model = MenuItem
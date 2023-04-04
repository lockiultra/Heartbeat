from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'menu/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class RegistrationView(CreateView):
    template_name = 'menu/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class LoginView(LoginView):
    template_name = 'menu/login.html'
    authenication_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
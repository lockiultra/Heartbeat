from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'menu/index.html'

class RegistrationView(CreateView):
    template_name = 'menu/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'menu/login.html', {'form': form})


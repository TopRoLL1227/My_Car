from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

class LoginInterfaceView(LoginView):
    template_name = 'my_car/login.html'
    next_page = '/'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)
    

class LogoutInterfaceView(LogoutView):
    next_page = '/'
    

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'my_car/register.html'
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)
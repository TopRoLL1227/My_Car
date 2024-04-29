from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import CustomUserCreationForm, CustomPasswordChangeForm, CustomUserEditForm
from .models import CustomUser


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


class ProfileView(UpdateView):
    model = CustomUser
    form_class = CustomUserEditForm
    template_name = 'profile.html'
    success_url = reverse_lazy('users:profile')


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('users:profile')
    template_name = 'change_password.html'

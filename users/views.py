
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages


from .forms import CustomUserCreationForm, CustomUserEditForm, CustomPasswordChangeForm
from .models import CustomUser


# Create your views here.


class MainView(TemplateView):

    template_name = 'app_templates/main.html'



class LoginInterfaceView(LoginView):
    template_name = 'app_templates/login.html'
    next_page = '/'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)
    

class LogoutInterfaceView(LogoutView):
    next_page = '/'


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'app_templates/register.html'
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)
    

class ProfileView(UpdateView):
    model = CustomUser
    form_class = CustomUserEditForm
    template_name = 'app_templates/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been successfully updated.')
        return super().form_valid(form)
    

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('users:profile')
    template_name = 'app_templates/change_password.html'

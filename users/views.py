from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from users.forms import CarForm
from django.contrib.auth.views import LoginView, LogoutView


class SignUpView(CreateView):
    form_class = CarForm
    success_url = reverse_lazy('login')
    template_name = 'my_car/register.html'


class Login(LoginView):
    template_name = 'my_car/login.html'


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main')
    else:
        return redirect('main')

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from users.forms import CarForm



class SignUpView(CreateView):
    form_class = CarForm
    success_url = reverse_lazy('login')
    template_name = 'my_car/register.html'




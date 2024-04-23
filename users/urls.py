from django.urls import path
from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name='signup')
]
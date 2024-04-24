from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [
    path("main/", views.MainView.as_view(), name='main'),
]
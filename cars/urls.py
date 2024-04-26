from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [
    path("", views.redirect_to_main),
    path("main/", views.MainView.as_view(), name='main'),
]
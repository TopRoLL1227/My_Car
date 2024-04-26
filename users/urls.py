from django.urls import path
from django.http import HttpResponse
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path("login/", views.Login.as_view(), name='login'),
    path("logout/", views.logout_user, name='logout'),
]

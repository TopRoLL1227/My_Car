from django.urls import path

from . import views
from cars.views import MainView

app_name = 'users'

urlpatterns = [

    path('', MainView.as_view(), name="main"),

    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/change_password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
]

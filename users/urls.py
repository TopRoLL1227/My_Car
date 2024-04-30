from django.urls import path

from .views import MainView, LoginInterfaceView, LogoutInterfaceView, SignupView, ProfileView, CustomPasswordChangeView

app_name = 'users'

urlpatterns = [
    path('', MainView.as_view(), name="main"),

    path('login', LoginInterfaceView.as_view(), name='login'),
    path('logout', LogoutInterfaceView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/change_password/', CustomPasswordChangeView.as_view(), name='change_password'),

]
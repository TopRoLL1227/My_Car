from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required


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
    template_name = 'my_car/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('users:profile')
    template_name = 'my_car/change_password.html'

@login_required
def update_personal_info(request):
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')  # Перенаправлення на сторінку профілю після успішної зміни інформації
    else:
        form = CustomUserEditForm(instance=request.user)
    return render(request, 'my_car/update_personal_info.html', {'form': form})

from django import forms
from users.models import CustomUser


class CarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'user_type']
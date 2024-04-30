from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE = [
        ('buyer', 'Покупець'),
        ('seller', 'Продавець')
    ]
    
    user_type = models.CharField(max_length=100, choices=USER_TYPE, null=True)


from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserModelManager



class CustomUser(AbstractUser):
    USER_TYPE = [
        ('buyer', 'Покупець'),
        ('seller', 'Продавець')
    ]
    user_type = models.CharField(max_length=100, choices=USER_TYPE, null=True)

    objects = UserModelManager()

    def __str__(self):
        return self.username
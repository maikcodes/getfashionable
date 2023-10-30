from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)

    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'User Accounts'

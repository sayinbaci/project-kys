# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext as _

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Model alanları
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # Diğer alanlar

    username = models.CharField(max_length=120, verbose_name='Kullanıcı Adı')
    email = models.EmailField(_('email address'), unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

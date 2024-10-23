# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext as _
from datetime import date



class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Model alanları
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # Diğer alanlar

    username = models.CharField(max_length=120, verbose_name='Kullanıcı Adı')
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=120, verbose_name='Adı')
    surname = models.CharField(max_length=120, verbose_name='Soyadı')
    identity_number = models.CharField(max_length=11,unique=True, verbose_name='TC Kimlik Numarası',
            validators=[
            RegexValidator(regex=r'^\d{11}$', message='TC kimlik numarası 11 rakam olmalıdır.')])
    phone = models.CharField(max_length=15, verbose_name='Telefon',
        validators=[
            RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Telefon numarası geçerli bir formatta olmalıdır.')
        ]
    )
    birth_date = models.DateField(default=date.today, null=True, blank=True)   
    address = models.TextField(max_length=250, verbose_name='Adres', default='Default Address')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    objects = CustomUserManager()

    def __str__(self):
        return  f'TC: {self.identity_number}, Telefon: {self.phone}, E-Posta Adresi: {self.email}'
    



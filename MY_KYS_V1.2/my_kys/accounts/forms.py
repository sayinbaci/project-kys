# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_recaptcha.fields import ReCaptchaField
from django import forms

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):
    captcha = ReCaptchaField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ("username","password")


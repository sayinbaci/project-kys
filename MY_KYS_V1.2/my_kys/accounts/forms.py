# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_recaptcha.fields import ReCaptchaField
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser




class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    address = forms.CharField(widget=forms.Textarea)
    birth_date = forms.DateField(
        label="Doğum Tarihi",
        required=False,
        widget=forms.DateInput(format="%d.%m.%Y", attrs={"type": "date"}),
        input_formats=["%d.%m.%Y"]
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email","identity_number", "name", "surname", "phone","birth_date","address")
      


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
      
        # Kullanıcının kendisi dışındaki kullanıcıları kontrol et
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError({'username': 'Bu kullanıcı adı zaten alınmış.'})

        if CustomUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise ValidationError({'email': 'Bu e-posta adresi zaten alınmış.'})

       
        return cleaned_data
        



class CustomUserChangeForm(UserChangeForm):
    captcha = ReCaptchaField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ("username","password")

class CustomUserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email","identity_number", "name", "surname", "phone","birth_date","address")

        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        # Kullanıcının kendisi dışındaki kullanıcıları kontrol et
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError({'username': 'Bu kullanıcı adı zaten alınmış.'})

        if CustomUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise ValidationError({'email': 'Bu e-posta adresi zaten alınmış.'})

        return cleaned_data
    
  
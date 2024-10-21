# accounts/views.py
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages

from .forms import CustomUserCreationForm,CustomUserChangeForm,CustomUserProfileForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
  

def LogInView(request):
    form = CustomUserChangeForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post:index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış.')  # Hata mesajı
            return render(request, 'accounts/form.html')  # Hata durumunda formu yeniden göster

    return render(request, "accounts/form.html", {"form": form, 'title': 'Giriş Yap'})


def SignUpView(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('accounts:login')

    return render(request, "accounts/form.html", {"form": form, 'title': 'Üye Ol'})

def ProfilUpdateView(request):
    
    user = request.user
    if request.method == 'POST':
        form = CustomUserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil başarıyla güncellendi.')  # Başarılı mesaj
            return redirect('accounts:profil')  # Güncellenmiş profil sayfasına yönlendirin
    else:
        form = CustomUserProfileForm(instance=user)

    return render(request, 'accounts/form.html', {'form': form, 'title': 'Profil Güncelle'})
    


def LogOutView(request):
    logout(request)
    return redirect('post:index')
# accounts/views.py
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView
from .forms import CustomUserCreationForm,CustomUserChangeForm,CustomUserProfileForm,CustomUser
from django.http import HttpRequest, HttpResponse
import datetime

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class UserListView(ListView):
    model = CustomUser
    template_name = 'accounts/user_list.html'
    context_object_name = 'users' 

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
    if request.method == 'POST':
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
    else:
        form = CustomUserCreationForm()

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

def UserListView(request):
    CustomUser = get_user_model()
    users = CustomUser.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})
   
def LogOutView(request):
    logout(request)
    return redirect('post:index')

def datetime_form(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            
            # Receive the submitted date as an instance of `datetime.date`.
            date: datetime.date = form.cleaned_data["birth_date"]
            # Do something with that value, such as storing it in a database
            # or displaying it to the user.
            date_output = date.strftime("%d.%m.%Y")
            print(date_output)
            return HttpResponse(f"The submitted date is: {date_output}")
    else:
        form = CustomUserCreationForm()
    ctx = {"form": form}
    return render(request, "accounts/form.html", ctx)
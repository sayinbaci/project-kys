from django.urls import path

from .views import *

app_name = "accounts"

urlpatterns = [

    path('signup/', SignUpView, name='signup'),
    path('login/', LogInView,name='login'),
    path('logout/', LogOutView,name='logout'),
    path('profil/', ProfilUpdateView,name='profil'),
    path('users/', UserListView, name='user_list'),
    path("datetime_form/", datetime_form, name="datetime_form")
   

]
from django.urls import path

from .views import *
from .utils import *

app_name = "accounts"

urlpatterns = [

    path('signup/', SignUpView, name='signup'),
    path('login/', LogInView,name='login'),
    path('logout/', LogOutView,name='logout'),
    path('profil/', ProfilUpdateView,name='profil'),
    path('user-list/', UserListView.as_view(), name='user_list'),
    path("datetime_form/", datetime_form, name="datetime_form"),
    path('load_cities_from_json/', load_cities_from_json, name='load_cities_from_json'),

]
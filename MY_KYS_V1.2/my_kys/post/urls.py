from django.urls import path, include
from .views import *

app_name = 'post'

urlpatterns = [
    path('index/', post_index,name='index'),
    path('create/', post_create,name='create'),


    path('details/<slug:slug>', post_details, name='details'),
    path('update/<slug:slug>', post_update, name='update'),
    path('delete/<slug:slug>', post_delete, name='delete'),
  

]
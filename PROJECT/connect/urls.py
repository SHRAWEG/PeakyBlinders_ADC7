from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create),
    path('read/', read),
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update), 
    path('delete/<int:id>', delete),   
]
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import search
 
urlpatterns = [
    path('search/',search),

]
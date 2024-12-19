from django.shortcuts import render
from django.urls import path
from .views import homepage, habitlist

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', habitlist, name='habitlist'),
]
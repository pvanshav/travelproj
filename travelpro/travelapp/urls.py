from django.contrib import admin
from django.urls import path

from travelapp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about.html',views.about,name='about')
]

from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('offers', views.offers, name='offers'),
    path('contact', views.contact, name='contact')
]

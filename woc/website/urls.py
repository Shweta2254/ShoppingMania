from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),

    path('about.html', views.about, name='about'),
    path('offers.html', views.offers, name='offers'),
    path('contact.html', views.contact, name='contact')
]

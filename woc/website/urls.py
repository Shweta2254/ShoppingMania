from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('offer', views.offer, name='offer'),
    path('contact', views.contact, name='contact')
]

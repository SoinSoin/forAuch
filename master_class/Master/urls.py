"""Master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url

from app_master import views

urlpatterns = [
    
    # Vous allez devoir réaliser ici le chemain de votre page d'accueil
    # Aidez-vous des commentaires en haut de la page
    # La vue à utiliser se nomme 'accueil'


    path('admin/', admin.site.urls),
]

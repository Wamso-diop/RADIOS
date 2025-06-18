"""
URL configuration for ECOMMERCE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [

    path('', index1, name = 'index1'),
    path('index/', index, name = 'index'),
    path('detail/<str:slug>', detail, name = 'detail'),
    path('detail/', detail, name = 'detail'),
    path('index2/', index2, name = 'index2'),
    path('panier/', panier, name = 'panier'),
    path('paiement/', paiement, name = 'paiement'),
    path('news/', news, name = 'news'),
    path('nopage/', nopage, name = "boutique"),
    path('contact/', contact, name = 'contact'),
    path("produit/<str:slug>/ajouteraupanier", ajouterAuPanier, name= "ajouteraupanier")
]

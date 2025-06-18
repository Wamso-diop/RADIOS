from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from .models import *  # Assurez-vous d'importer le modèle Produit

def ajouterAuPanier(request, slug):
    user  = request.user
    produit = get_object_or_404(Produit, slug=slug)
    panier,_ = Panier.objects.get_or_create(user=user)
    commande, estCreer = Commande.objects.get_or_create(user=user, produit=produit)
    if estCreer:
        panier.objects.add()
        panier.save()
    else:
        commande.quantite += 1
        commande.save
    return redirect(reverse("detail", kwargs={"slug":slug}))

def index(request):

    data = {
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/index.html", context=data)
def index1(request):

    data = {
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/index1.html", context=data)
def detail(request, slug):
    produit = Produit.objects.get(slug=slug)
    data = {
        'produit': produit,
        'images': produit.images.all(),  # Récupère toutes les images associées au produit
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/product_detail.html", context=data)
def detail(request):
    produit = Produit.objects.all()
    data = {
        'produit': produit,
        'images': produit.images.all(),  # Récupère toutes les images associées au produit
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/product_detail.html", context=data)
def panier(request):

    data = {
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/panier.html", context=data)

def paiement(request):
    data = {
        'aujoudhui': timezone.now()
    }
    return render(request, "boutique/paiement.html",context=data)


def news(request):
    data = {
        'aujourdhui': timezone.now()
    }
    return render(request, 'boutique/news.html', context=data)

def boutique(request):
    data = {
        'aujourdhui': timezone.now()
    }
    return render(request, 'boutique/boutique.html', context=data)
def contact(request):
    data = {
        'aujourdhui': timezone.now()
    }
    return render(request, 'boutique/contact.html', context=data)
def index2(request):
    data = {
        'aujourdhui': timezone.now()
    }
    return render(request, 'boutique/index2.html', context=data)
def nopage(request):
    data = {
        'aujourdhui': timezone.now()
    }
    return render(request, 'boutique/404.html', context=data)

def genererRecu(request):
    data={
        'aujourdhui':timezone.now
    }
    return render(request, 'boutique/connexion.html', context=data)


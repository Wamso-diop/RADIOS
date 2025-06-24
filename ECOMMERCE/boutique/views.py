from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from boutique.models import *  # Assurez-vous d'importer le modèle Produit
from utilisateur.models import Utilisateur
def ajouterAuPanier(request, slug):
    user  = request.user
    quantite = request.POST.get("product-count")
    produit = get_object_or_404(Produit, slug=slug)
    panier,_ = Panier.objects.get_or_create(utilisateur=user)
    commande, estCreer = Commande.objects.get_or_create(utilisateur=user, produit=produit, quantite=quantite)
    if estCreer:
        panier.commandes.add(commande)
        panier.save()
    else:
        commande.quantite += 1
        commande.save()
    return redirect(reverse("detail_slug", kwargs={"slug":slug}))

def index(request):

    data = {
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/index.html", context=data)
def index1(request):
    camera1 = Produit.objects.filter(slug="camera-surveillance-4k").first()  # Récupère le produit avec le slug "camera-surveillance-4k"
    topproduits = Produit.objects.filter(est_nouveau=True).order_by('-date_ajout')[:8]  # Récupère les 5 derniers produits ajoutés
    if not camera1:
        print("Produit non trouvé avec le slug 'camera-surveillance-4k'")
        return render(request, "boutique/index1.html", context={'error': 'Produit non trouvé'})
    images = ImageProduit.objects.filter(produit=camera1)  # Récupère toutes les images associées au produit
    data = {
        'produit': camera1,
        'images': images,
        'topproduits': topproduits,
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/index.html", context=data)
def detail_slug(request, slug):
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
    panier = get_object_or_404(Panier, Utilisateur = request.user)
    prix_total = 0
    for commande in panier.commandes.all():
        prix_total += commande.produit.prix * commande.quantite

    data = {
        'panier': panier,
        'prix_total': prix_total,
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


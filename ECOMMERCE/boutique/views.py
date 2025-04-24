from django.utils import timezone

from django.shortcuts import render



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
def detail(request):

    data = {
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
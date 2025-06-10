from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def inscription(request):
    data={
        'aujourdhui':timezone.now
    }
    return render(request, 'utilisateur/inscription.html', context=data)
def connexion(request):
    data={
        'aujourdhui':timezone.now
    }
    return render(request, 'boutique/inscription.html', context=data)

def deconnexion(request):
    data={
        'aujourdhui':timezone.now
    }
    return render(request, 'boutique/connexion.html', context=data)
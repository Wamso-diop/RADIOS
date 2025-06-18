from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
import re
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def inscription(request):
    """
    Vue pour l'inscription d'un utilisateur
    """
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        username = email  # Username basé sur l'email
       

        errors = []

        if not first_name:
            errors.append("Le prénom est obligatoire.")
        if not last_name:
            errors.append("Le nom est obligatoire.")
        if not email:
            errors.append("L'email est obligatoire.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("L'email n'est pas valide.")
        if not password or not re.match(r'^(?=.*[A-Z])(?=.*\d).{8,}$', password):
            errors.append("Le mot de passe doit contenir au moins 8 caractères, une majuscule et un chiffre.")

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'utilisateur/inscription.html')
        user = User.objects.filter(username=username).first()
        if user:
            # L'utilisateur existe déjà, on tente de l'authentifier
            print("L'utilisateur existe déjà, tentative de connexion.")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Bienvenue, vous êtes connecté.")
                return redirect('index')
            else:
                messages.error(request, "Mot de passe incorrect.")
                return render(request, 'utilisateur/inscription.html')
        else:
            # Création de l'utilisateur
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            messages.success(request, "Inscription réussie ! Bienvenue.")
            return redirect('index')

    return render(request, 'utilisateur/inscription.html')
def connexion(request):
    """
    Vue pour la connexion d'un utilisateur
    """
    if request.method == 'POST':
        username = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Veuillez remplir tous les champs.")
            return render(request, 'utilisateur/inscription.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('index')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return render(request, 'utilisateur/inscription.html')

    return render(request, 'utilisateur/inscription.html')

def deconnexion(request):
    logout(request)
    return render(request, 'boutique/inscription.html')
from django.contrib import admin

from .models import Utilisateur  # Importez votre modèle

# Enregistrement simple
admin.site.register(Utilisateur)
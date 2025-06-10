from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(AbstractUser):
    """
    Modèle Utilisateur
    """
    telephone = models.CharField(max_length=15, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    quartier = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.username
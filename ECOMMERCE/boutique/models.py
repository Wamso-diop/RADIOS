from django.db import models
from django.urls import reverse
class ImageProduit(models.Model):
    produit = models.ForeignKey(
        "Produit", 
        on_delete=models.CASCADE,
        related_name='images'  # Important pour accéder aux images depuis un produit
    )
    image = models.ImageField(upload_to='produits/images/')
    ordre = models.PositiveIntegerField(default=0)  # Optionnel pour trier les images

    class Meta:
        ordering = ['ordre']  # Trier les images par ordre

    def __str__(self):
        return f"Image {self.id} pour {self.produit.nom}"
# Create your models here.
class Produit(models.Model):
    """
    Modèle Produit
    """
    nom = models.CharField(max_length=255)
    description = models.TextField( verbose_name="Description")
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    date_ajout = models.DateTimeField(auto_now_add=True)
    est_nouveau = models.BooleanField(default=True, verbose_name="Nouveau")
    image_principale = models.ImageField(upload_to='produits/images/', blank=True, null=True, verbose_name="Image Principale", help_text="Image principale du produit")
    nombre_etoile  = models.IntegerField(default=0, verbose_name="Étoiles", help_text="Note de 0 à 5")
    slug = models.SlugField(max_length=128, unique=True, verbose_name="Slug", help_text="Identifiant unique pour le produit")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, verbose_name="Catégorie", related_name='produits', help_text="Catégorie du produit")
    def __str__(self):
        return f"{self.nom} ({self.prix})"
    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
class Categorie(models.Model):
    """
    Modèle Categorie
    """
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nom
class Panier(models.Model):
    """
    Modèle Panier
    """
    utilisateur = models.ForeignKey('utilisateur.Utilisateur', on_delete=models.CASCADE)
    est_commande = models.BooleanField(default=False, verbose_name="Commandé", help_text="Indique si le panier a été commandé")
    commandes = models.ManyToManyField('Commande', blank=True, related_name='paniers', verbose_name="Commandes", help_text="Commandes associées à ce panier")
    date_commande = models.DateTimeField(auto_now_add=True,blank=True, null=True, verbose_name="Date de commande", help_text="Date à laquelle le panier a été commandé")
    def __str__(self):
        return f"Panier de {self.utilisateur.username}"
    class Meta:
        verbose_name = "Panier"
        verbose_name_plural = "Paniers"
        ordering = ['utilisateur', 'date_commande']
class Commande(models.Model):
    """
    Modèle Commande
    """
    utilisateur = models.ForeignKey('utilisateur.Utilisateur', on_delete=models.CASCADE, verbose_name="Utilisateur")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="Produit")
    adresse_livraison = models.CharField(max_length=255)
    statut = models.CharField(max_length=50, choices=[('en_attente', 'En attente'), ('envoyé', 'Envoyé'), ('livré', 'Livré')], default='en_attente')
    mode_paiement = models.CharField(max_length=50, choices=[('carte', 'Carte'), ('paypal', 'PayPal'), ('mobile', 'Mobile')], default='mobile')
    quantite = models.PositiveIntegerField(default=1)
    date_livraison = models.DateTimeField(blank=True, null=True)
    date_modification = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'commande'
        verbose_name_plural = 'commandes'
    def __str__(self):
        return f"Commande de {self.utilisateur.username} - {self.produit.nom}" 
    def get_total_price(self):
        return self.produit.prix * self.quantite
    def get_total_price_with_shipping(self):
        return self.get_total_price() + 10
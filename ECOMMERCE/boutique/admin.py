from django.contrib import admin
from .models import *

class ImageProduitInline(admin.TabularInline):  # ou admin.StackedInline
    model = ImageProduit
    extra = 1  # Nombre de formulaires vides affichés

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    inlines = [ImageProduitInline]
    list_display = ('nom', 'prix')

@admin.register(ImageProduit)
class ImageProduitAdmin(admin.ModelAdmin):
    list_display = ('produit', 'image_preview')
    
    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}"/>', obj.image.url)
        return ""
    image_preview.short_description = 'Aperçu'

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','description')

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ("utilisateur","produit","statut","mode_paiement","quantite","date_livraison","date_modification")
@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ("utilisateur","date_commande", "est_commande")
# Generated by Django 5.2 on 2025-06-21 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(verbose_name='Description')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('est_nouveau', models.BooleanField(default=True, verbose_name='Nouveau')),
                ('image_principale', models.ImageField(blank=True, help_text='Image principale du produit', null=True, upload_to='produits/images/', verbose_name='Image Principale')),
                ('nombre_etoile', models.IntegerField(default=0, help_text='Note de 0 à 5', verbose_name='Étoiles')),
                ('slug', models.SlugField(help_text='Identifiant unique pour le produit', max_length=128, unique=True, verbose_name='Slug')),
                ('categorie', models.ForeignKey(help_text='Catégorie du produit', on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='boutique.categorie', verbose_name='Catégorie')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.produit')),
            ],
            options={
                'verbose_name': 'Panier',
                'verbose_name_plural': 'Paniers',
                'ordering': ['utilisateur', 'produit'],
            },
        ),
        migrations.CreateModel(
            name='ImageProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='produits/images/')),
                ('ordre', models.PositiveIntegerField(default=0)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='boutique.produit')),
            ],
            options={
                'ordering': ['ordre'],
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse_livraison', models.CharField(max_length=255)),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('envoyé', 'Envoyé'), ('livré', 'Livré')], default='en_attente', max_length=50)),
                ('mode_paiement', models.CharField(choices=[('carte', 'Carte'), ('paypal', 'PayPal'), ('mobile', 'Mobile')], default='mobile', max_length=50)),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('date_livraison', models.DateTimeField(blank=True, null=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.produit', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'commande',
                'verbose_name_plural': 'commandes',
            },
        ),
    ]

# Generated by Django 5.2 on 2025-06-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='quartier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='ville',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

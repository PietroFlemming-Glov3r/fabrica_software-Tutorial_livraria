# Generated by Django 5.0.3 on 2024-03-21 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0001_initial'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-27 15:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0006_itenscompra_preco_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo_pagamento',
            field=models.IntegerField(choices=[(1, 'Cartão de Crédito'), (2, 'Cartão de Débito'), (3, 'Pix'), (4, 'Boleto'), (5, 'Transferência Bancária'), (6, 'Dinheiro'), (7, 'Outro')], default=1),
        ),
    ]

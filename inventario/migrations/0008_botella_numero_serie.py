# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_barril_numero_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='botella',
            name='Numero_serie',
            field=models.IntegerField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True),
        ),
    ]
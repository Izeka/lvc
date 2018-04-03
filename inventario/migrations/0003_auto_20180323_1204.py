# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20180301_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lupulo',
            name='Alfa_Acido',
            field=models.FloatField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0053_auto_20171124_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='coccion',
            name='Tiempo_Filtrado',
            field=models.IntegerField(default=None, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AddField(
            model_name='coccion',
            name='Tiempo_Lavado',
            field=models.IntegerField(default=None, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AddField(
            model_name='receta',
            name='Tiempo_Filtrado',
            field=models.IntegerField(default=None, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AddField(
            model_name='receta',
            name='Tiempo_Lavado',
            field=models.IntegerField(default=None, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
    ]

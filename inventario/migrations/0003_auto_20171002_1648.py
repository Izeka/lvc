# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_remove_agregados_x_receta_agregados'),
        ('contabilidad', '0002_compra'),
        ('inventario', '0002_auto_20171002_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agregado',
            name='insumo_ptr',
        ),
        migrations.DeleteModel(
            name='Agregado',
        ),
    ]
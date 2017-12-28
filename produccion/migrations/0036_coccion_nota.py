# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0035_remove_coccion_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='coccion',
            name='Nota',
            field=models.TextField(default='0', error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100),
        ),
    ]
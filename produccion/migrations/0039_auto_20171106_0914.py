# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_agregado'),
        ('produccion', '0038_auto_20171106_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agregados_x_Coccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100)),
                ('Tiempo', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'})),
                ('Agregados', models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='inventario.Agregado')),
            ],
        ),
        migrations.CreateModel(
            name='Coccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DI', models.CharField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100)),
                ('Temp_Maceracion', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'})),
                ('Tiempo_Maceracion', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'})),
                ('Tiempo_Hervor', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'})),
                ('Temp_Final', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'})),
                ('DF', models.CharField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100)),
                ('Litros', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'})),
                ('IBUs', models.FloatField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True)),
                ('EBC', models.IntegerField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True)),
                ('Eficiencia', models.IntegerField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True)),
                ('Alcohol', models.FloatField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True)),
                ('Nota', models.TextField(default='0', error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100)),
                ('Receta', models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Receta')),
            ],
        ),
        migrations.CreateModel(
            name='Levadura_x_Coccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100)),
                ('Coccion', models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Coccion')),
                ('Levadura', models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='inventario.Levadura')),
            ],
        ),
        migrations.CreateModel(
            name='Lupulo_x_Coccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100)),
                ('Tiempo', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'})),
                ('Coccion', models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Coccion')),
                ('Lupulo', models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='inventario.Lupulo')),
            ],
        ),
        migrations.CreateModel(
            name='Malta_x_Coccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100)),
                ('Coccion', models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Coccion')),
                ('Malta', models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='inventario.Malta')),
            ],
        ),
        migrations.AddField(
            model_name='agregados_x_coccion',
            name='Coccion',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Coccion'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-02 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vale_consumo', '0008_centro_costo_cc_centro_costo_comentario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='edificio',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='unidad_negocio',
        ),
    ]
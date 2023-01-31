# Generated by Django 4.1.5 on 2023-01-31 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id_bodega', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_bodega', models.CharField(max_length=100)),
                ('is_active_bodega', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('is_active_categoria', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Centro_Costo',
            fields=[
                ('id_centro_costo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_centro_costo', models.CharField(max_length=100)),
                ('is_active_centro_costo', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
            options={
                'verbose_name': 'Centro de Costo',
                'verbose_name_plural': 'Centros de Costos',
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id_recurso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_recurso', models.CharField(max_length=100)),
                ('unidad', models.CharField(choices=[('Unidad 1', 'Unidad 1'), ('Unidad 2', 'Unidad 2'), ('Unidad 3', 'Unidad 3')], default='Unidad 1', max_length=10)),
                ('is_active_recurso', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('categoria_recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vale_consumo.categoria')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateField()),
                ('edificio', models.IntegerField()),
                ('piso', models.IntegerField()),
                ('estado_solicitud', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Entregado', 'Entregado'), ('Rechazado', 'Rechazado')], default='Pendiente', max_length=10)),
                ('is_active_solicitud', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vale_consumo.bodega')),
                ('id_centro_costo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vale_consumo.centro_costo')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
            },
        ),
        migrations.CreateModel(
            name='Unidad_Negocio',
            fields=[
                ('id_unidad_negocio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_unidad_negocio', models.CharField(max_length=100)),
                ('is_active_unidad_negocio', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
            options={
                'verbose_name': 'Unidad de Negocio',
                'verbose_name_plural': 'Unidades de Negocios',
            },
        ),
        migrations.CreateModel(
            name='Solicitud_Recurso',
            fields=[
                ('id_solicitud_recurso', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_solicitada', models.IntegerField()),
                ('estado_despacho', models.CharField(choices=[('No realizado', 'No realizado'), ('Realizado', 'Realizado')], default='No realizado', max_length=15)),
                ('id_recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vale_consumo.recurso')),
                ('id_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vale_consumo.solicitud')),
            ],
            options={
                'verbose_name': 'Solicitud de Recurso',
                'verbose_name_plural': 'Solicitudes de Recursos',
            },
        ),
        migrations.AddField(
            model_name='solicitud',
            name='unidad_negocio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vale_consumo.unidad_negocio'),
        ),
        migrations.AddField(
            model_name='centro_costo',
            name='unidad_negocio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vale_consumo.unidad_negocio'),
        ),
    ]

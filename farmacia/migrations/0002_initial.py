# Generated by Django 4.2.7 on 2023-11-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmacia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=255)),
                ('laboratorio', models.CharField(max_length=255)),
                ('principio_activo', models.CharField(max_length=255)),
                ('accion_terapeutica', models.CharField(max_length=255)),
                ('presentacion', models.CharField(max_length=255)),
                ('dosis', models.CharField(max_length=255)),
                ('bioequivalente', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proveedor', models.CharField(max_length=255)),
                ('nivel_stock', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('razon_social', models.CharField(max_length=255)),
                ('rut', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('fono', models.CharField(max_length=20)),
                ('productos', models.TextField()),
            ],
        ),
    ]

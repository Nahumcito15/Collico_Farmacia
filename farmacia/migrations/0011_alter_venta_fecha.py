# Generated by Django 4.2.7 on 2023-11-21 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0010_venta_vendedor_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

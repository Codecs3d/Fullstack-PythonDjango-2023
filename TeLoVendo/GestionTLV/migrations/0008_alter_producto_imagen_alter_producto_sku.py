# Generated by Django 4.2.1 on 2023-06-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTLV', '0007_alter_detalle_total_alter_producto_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.CharField(max_length=50),
        ),
    ]
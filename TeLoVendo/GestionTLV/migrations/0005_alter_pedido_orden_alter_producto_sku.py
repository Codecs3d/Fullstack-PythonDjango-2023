# Generated by Django 4.2.1 on 2023-06-02 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTLV', '0004_alter_pedido_orden_alter_producto_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='orden',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.CharField(default='060201094523', max_length=50),
        ),
    ]

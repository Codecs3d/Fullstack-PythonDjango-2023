# Generated by Django 4.2.1 on 2023-06-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTLV', '0003_alter_producto_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='orden',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.CharField(default='060201082423', max_length=50),
        ),
    ]

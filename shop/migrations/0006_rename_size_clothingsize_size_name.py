# Generated by Django 4.1.7 on 2023-03-25 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_quantity_inventory_product_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothingsize',
            old_name='size',
            new_name='size_name',
        ),
    ]
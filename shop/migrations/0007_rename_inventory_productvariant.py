# Generated by Django 4.1.7 on 2023-03-27 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_size_clothingsize_size_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventory',
            new_name='ProductVariant',
        ),
    ]

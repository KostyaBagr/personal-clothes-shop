# Generated by Django 4.1.7 on 2023-03-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_clothingsize_options_alter_inventory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_preview',
            field=models.ImageField(upload_to='images/%Y/%m'),
        ),
    ]

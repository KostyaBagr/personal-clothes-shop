# Generated by Django 4.1.7 on 2023-03-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clothingsize',
            options={'verbose_name': 'Размеры товаров'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Кол-во товаров на складе', 'verbose_name_plural': 'Кол-во товаров на складе'},
        ),
        migrations.AlterModelOptions(
            name='productphotos',
            options={'verbose_name': 'Фото товара'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m'),
        ),
    ]

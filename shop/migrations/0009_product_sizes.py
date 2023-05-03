# Generated by Django 4.1.7 on 2023-03-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_product_sizes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(through='shop.ProductVariant', to='shop.clothingsize'),
        ),
    ]
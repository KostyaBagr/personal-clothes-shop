from django.contrib.auth.models import User
from django.db import models
import re
# Create your models here.
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/%Y/%m')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',
                                 related_name='products',
                                 on_delete=models.CASCADE)

    sizes = models.ManyToManyField('ClothingSize', through='ProductVariant')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])
class ProductPhotos(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m')
    post = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фото товара'


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"cat_slug": self.slug})


class ClothingSize(models.Model):
    size_choices = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )
    size_name = models.CharField(max_length=2, choices=size_choices, blank=True, null=True)
    class Meta:

        verbose_name = 'Размеры товаров'

    def __str__(self):
        return self.size_name



class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ClothingSize, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product} ({self.product_size}): {self.product_quantity} в наличии"

    class Meta:

        unique_together = ('product', 'product_size')

        verbose_name = 'Кол-во товаров на складе'
        verbose_name_plural = 'Кол-во товаров на складе'




@receiver(pre_delete, sender=Product)
def image_model_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)

@receiver(pre_delete, sender=ProductPhotos)
def image_model_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)
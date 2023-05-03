from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductPhotos
from .forms import *
from mycart.forms import *
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
# Create your views here.
def main_page(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    dict ={

        'products':products,
        'categories':categories,


    }
    return render(request, 'shop/main.html', dict)

def show_category(request, cat_slug):
    products = Product.objects.filter(category__slug=cat_slug)
    categories = Category.objects.all()
    dict = {
        'products': products,
        'categories': categories,
        'cat_selected' : cat_slug,
    }
    return render(request, 'shop/main.html', dict)


def detail_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    get_all_photos = ProductPhotos.objects.filter(post=product)
    sizes = product.sizes.all()
    cart_product_form = AddProductInCart(request.POST)
    selected_size = None

    if request.method == 'POST':

        selected_size_id = request.POST.get('size')
        selected_size = get_object_or_404(ClothingSize, id=selected_size_id)
        print(selected_size, product)
    context = {
        'get_all_photos':get_all_photos,
        'product': product,
        'sizes': sizes,
        'cart_product_form':cart_product_form,
        'selected_size': selected_size,
    }

    return render(request, 'shop/details.html', context)












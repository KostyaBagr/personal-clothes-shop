from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

from mycart.forms import AddProductInCart

# # Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import ProductVariant, Product
from mycart.cart import Cart

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def cart_details(request):
    cart = Cart(request)
    print(request.session.items())
    return render(request, 'mycart/cart_details.html', {'cart':cart})

@require_http_methods(["GET", "POST"])
def add_cart(request, variant_id):
    cart = Cart(request)
    product = get_object_or_404(ProductVariant, id=variant_id)
    print(product.name)
    form = AddProductInCart(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],update=cd['update'])

    return redirect('mycart:cart_detail')
# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(ProductVariant, id=product_id)
#     form = AddProductInCart(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  product_size=cd['size'])
#
#     return redirect('cart_detail')
#
# def cart_details(request):
#     cart = Cart(request)
#     for i in cart:
#         i['override_quantity_form'] = AddProductInCart(initial={'quantity':i['quantity'],
#                                                                 'update':True,
#                                                                     'product_size':i['product_size']})
#     return render(request, 'cart/cart_details.html', {'cart':cart})
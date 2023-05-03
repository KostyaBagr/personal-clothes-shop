from django.urls import path
from .views import *

app_name ='mycart'
urlpatterns = [
    path('', cart_details,name ='cart_detail'),
    path('add/<int:variant_id>/', add_cart,name='add_cart')

]
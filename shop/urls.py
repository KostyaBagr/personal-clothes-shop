from django.urls import path
from .views import *
urlpatterns =[
    path('', main_page, name='main_page'),
    path('category/<slug:cat_slug>/',show_category, name='category'),
    path('product/<slug:product_slug>/', detail_product, name='product'),



]
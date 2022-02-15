from django.shortcuts import render

from rest_framework import viewsets

from cart.forms import CartAddProductForm
from viewshop.models import Product
from viewshop.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def main_page(request):
    products = Product.objects.all()
    category = set()
    for m in products:
        category.add(m.category)

    return render(request,
                  'viewshop/main.html',
                  {'title': 'Main page', 'category': category, 'products': products})


def category_products(request, category):
    fff = Product.objects.all()
    category_list = set()
    for m in fff:
        category_list.add(m.category)
    available = Product.objects.filter(category=category)
    return render(request, 'viewshop/index.html', {'available': available, 'category_list': category_list})


def product(request, product_name):
    product_detail = Product.objects.filter(title=product_name)
    cart_product_form = CartAddProductForm()
    return render(request, 'viewshop/product_details.html',
                  {'product_detail': product_detail,
                   'title': 'Products detail', "cart_product_form": cart_product_form})





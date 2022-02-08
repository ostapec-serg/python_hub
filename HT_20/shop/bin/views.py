from django.shortcuts import render, redirect

from bin.models import UserCart
from viewshop.models import Product


def user_cart(request):
    product_in_cart = UserCart.objects.all()
    full_price = []
    for price in product_in_cart:
        full_price.append(int(price.goods_ids.price))
    return render(request, 'bin/bin.html',
                  {'product_in_cart': product_in_cart,
                   'full_price': sum(full_price)})


def add_to_cart(request):
    some = request.POST['id']
    cart = UserCart()
    cart.client_name = request.POST['username']
    cart.goods_ids = Product.objects.get(pk=some)
    cart.save()
    return redirect('/')


def remove_from_cart(request, pk):
    remove_product = UserCart.objects.filter(id=pk)
    remove_product.delete()
    return redirect('/cart/')

from django.shortcuts import render, redirect

from favorites.models import UserFavorites
from viewshop.models import Product


def user_favorites(request):
    product_in_cart = UserFavorites.objects.all()
    full_price = []
    for price in product_in_cart:
        full_price.append(int(price.goods_ids.price))
    return render(request, 'bin/bin.html',
                  {'product_in_cart': product_in_cart,
                   'full_price': sum(full_price)})


def add_to_favorites(request):
    some = request.POST['id']
    cart = UserFavorites()
    cart.client_name = request.POST['username']
    cart.goods_ids = Product.objects.get(pk=some)
    cart.save()
    return redirect('/')


def remove_from_favorites(request, pk):
    remove_product = UserFavorites.objects.filter(id=pk)
    remove_product.delete()
    return redirect('/cart/')

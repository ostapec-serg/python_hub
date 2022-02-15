from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from viewshop.models import Product


@require_POST
def add_to_cart(request):
    if is_ajax(request=request) and request.POST:
        cart = Cart(request)
        product = get_object_or_404(Product, id=request.POST['product_id'])
        form = CartAddProductForm(request.POST)
        valid = form.is_valid()
        if valid:
            cd = form.cleaned_data
            cart.add_to_cart(product=product,
                             quantity=cd['quantity'],
                             update_quantity=cd['update'])
        product_price = cart.cart[request.POST['product_id']]['price']
        product_quantity = cart.cart[request.POST['product_id']]['quantity']
        product_total_price = int(product_price) * product_quantity
        total_price = cart.total_price()
        cart_product = len(cart.cart)
        product_amount = []
        for item in cart.cart:
            if item == request.POST['product_id']:
                product_amount = cart.cart[item]['quantity']
        return JsonResponse({'cart_product': cart_product,
                             'product_amount': product_amount,
                             'total_price': total_price,
                             'product_total_price': product_total_price},
                            content_type='aplication/json')

    else:
        data = {'massage': f"OOOOps! something go wrong!"}
        return HttpResponse(data, content_type='aplication/json')


def quantity_remove_from_cart(request):
    if is_ajax(request=request) and request.POST:
        cart = Cart(request)
        product = get_object_or_404(Product, id=request.POST['product_id'])
        form = CartAddProductForm(request.POST)
        product_price = cart.cart[request.POST['product_id']]['price']
        product_quantity = cart.cart[request.POST['product_id']]['quantity']
        product_total_price = int(product_price) * product_quantity
        total_price = cart.total_price()
        if form.is_valid():
            cd = form.cleaned_data
            cart.quantity_remove(product=product,
                                 quantity=cd['quantity'])
        cart_product = len(cart.cart)
        product_amount = []
        for item in cart.cart:
            if item == request.POST['product_id']:
                product_amount = cart.cart[item]['quantity']
        return JsonResponse({'cart_product': cart_product,
                             'product_amount': product_amount,
                             'total_price': total_price,
                             'product_total_price': product_total_price
                             },
                            content_type='aplication/json')

    else:
        data = {'massage': f"OOOOps! something go wrong!"}
        return HttpResponse(data, content_type='aplication/json')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:view_cart')


def view_cart(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})
    return render(request, 'cart/cart.html', {'cart': cart})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

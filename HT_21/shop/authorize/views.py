from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import UpdateView

from authorize.form import LoginForm, ProductForm
from viewshop.models import Product


class UserAuth(LoginView):
    form_class = LoginForm
    template_name = 'authorize/login.html'


class EditProduct(UpdateView):
    model = Product
    template_name = 'viewshop/edit_product.html'
    form_class = ProductForm


def delete_product(request, pk):
    delete_item = Product.objects.filter(pk=pk)
    delete_item.delete()
    return redirect('/')


def logout_user(request):
    logout(request)


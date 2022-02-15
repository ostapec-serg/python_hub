from django.db import models

from viewshop.models import Product


class UserFavorites(models.Model):
    client_name = models.CharField(max_length=150)
    goods_ids = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.goods_ids


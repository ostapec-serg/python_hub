from django.db import models


class Product(models.Model):
    category = models.CharField('Category name', max_length=250)
    title = models.CharField('Product name', max_length=250)
    description = models.TextField('Product description')
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    active_status = models.BooleanField(default=False)
    product_img = models.ImageField(null=True, upload_to='photos/ ', blank='true', verbose_name='Photo')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/product/{self.title}"

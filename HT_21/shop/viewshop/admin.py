from django.contrib import admin

from viewshop.models import Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'product_img', 'price', 'quantity')
    list_display_links = ('title', 'description',)


admin.site.register(Product, CategoryAdmin)

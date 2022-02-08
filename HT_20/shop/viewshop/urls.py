from django.urls import pathfrom viewshop import viewsfrom authorize.views import EditProduct, delete_productfrom django.conf.urls.static import staticfrom django.conf import settingsapp_name = 'viewshop'urlpatterns = [    path('', views.main_page, name='view_shop'),    path('product/<product_name>', views.product, name='product'),    path('edit/<int:pk>', EditProduct.as_view(), name='edit'),    path('delete/<int:pk>', delete_product, name='delete'),    path('<category>/', views.category_products, name='category_products'),] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
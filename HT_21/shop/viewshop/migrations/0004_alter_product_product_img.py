# Generated by Django 4.0.1 on 2022-02-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewshop', '0003_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank='true', upload_to='photos/%Y/%m/%d/ ', verbose_name='Photo'),
        ),
    ]

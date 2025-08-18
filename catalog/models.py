from django.db import models

from users.models import CustomUser


class Category(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='product/image', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Дата создания', blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', blank=True, null=True, auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец', blank=True, null=True)
    is_published = models.BooleanField(verbose_name='Признак публикации', default=False)

    def __str__(self):
        return f'{self.category}: {self.product_name} - {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name']
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product')
        ]

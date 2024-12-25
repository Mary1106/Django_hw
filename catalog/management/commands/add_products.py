from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test product to the DB'

    def handle(self, *args, **kwargs):
        # Удаление все продуктов и категорий из БД перед добавлением тестовых:
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(category_name='Товары для животных', description='Надо брать')

        products = [
            {
                'product_name': 'Зеркало для попугайчика',
                'description': 'Круглое',
                'category': category,
                'price': '150'
        },
            {
                'product_name': 'Корм для хомячков',
                'description': 'Зерно и сено',
                'category': category,
                'price': '550'
            }
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт {product.product_name} добавлен'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт {product.product_name} уже существует'))

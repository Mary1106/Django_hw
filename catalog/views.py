from django.shortcuts import render
from .models import Product


def home(request):
    """Функция-контроллер, рендерит шаблон страницы home со списком всех продуктов БД"""

    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def contacts(request):
    """Функция-контроллер, рендерит шаблон страницы contacts"""

    return render(request, 'contacts.html')


def product_detailed(request, pk):
    """Функция-контроллер, рендерит шаблон страницы product"""

    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detailed.html', context)

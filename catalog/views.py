from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .forms import ProductForm, ProductModeratorForm
from .models import Product, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .services import get_products_from_cache, get_products_by_category


class CategoriesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductsByCategoryListView(ListView):
    model = Category
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products_by_category'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductListView(CategoriesMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = get_products_from_cache()
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return queryset
        else:
            return queryset.filter(is_published=True)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(CategoriesMixin, LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(CategoriesMixin, LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return redirect('catalog:product_list')


class ProductUpdateView(CategoriesMixin, LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.can_delete_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(CategoriesMixin, LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        user = self.request.user
        product = super().get_object(queryset)
        if user == product.owner or user.has_perm('catalog.can_delete_product'):
            return product
        raise PermissionDenied


def contacts(request):
    """Функция-контроллер, рендерит шаблон страницы contacts"""

    categories = Category.objects.all()
    return render(request, 'contacts.html', {'categories': categories})

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    contacts, ProductsByCategoryListView, test_view

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', ProductsByCategoryListView.as_view(), name='category_detail'),
]

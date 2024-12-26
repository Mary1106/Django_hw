from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detailed

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_detailed/<int:pk>', product_detailed, name='product_detailed'),
]

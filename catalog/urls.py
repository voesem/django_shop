from django.urls import path

from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path(r'product/(?P<product_id>\w+)\$', views.product, name='product')
]

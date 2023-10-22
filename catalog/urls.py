from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product')
]

from django.urls import path
from django.views.decorators.cache import never_cache

from . import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='update_product')
]

from django.urls import path
from django.views.decorators.cache import never_cache

from blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('create/', never_cache(PostCreateView.as_view()), name='create'),
    path('', PostListView.as_view(), name='list'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view_post'),
    path('edit/<int:pk>/', never_cache(PostUpdateView.as_view()), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete')
]

# urls.py
from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView
from . import views


urlpatterns = [
    # ... other URL patterns ...
    path('search/', views.product_search, name='product_search'),


    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),


    # Category URLs
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('category/list/', views.CategoryListView.as_view(), name='category_list'),


    path('manufacturer/create/', views.ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('manufacturer/update/<int:pk>/', views.ManufacturerUpdateView.as_view(), name='manufacturer_update'),
    path('manufacturer/delete/<int:pk>/', views.ManufacturerDeleteView.as_view(), name='manufacturer_delete'),
    path('manufacturer/list/', views.ManufacturerListView.as_view(), name='manufacturer_list'),

    # Tag URLs
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag/update/<int:pk>/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag/delete/<int:pk>/', views.TagDeleteView.as_view(), name='tag_delete'),
    path('tag/list/', views.TagListView.as_view(), name='tag_list'),
]


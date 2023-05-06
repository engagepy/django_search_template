from django.shortcuts import render
# views.py
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product, Category, Tag, Manufacturer

from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'  # Change this to your template

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__name__icontains=search_query) |
                Q(tags__name__icontains=search_query) |
                Q(manufacturer__name__icontains=search_query)
            ).distinct()

        return queryset

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'category', 'tags', 'manufacturer']
    template_name = 'product/product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'category', 'tags', 'manufacturer', 'created_by']
    template_name = 'product/product_update.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')
    template_name = 'product/product_confirm_delete.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'product/category_create.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'product/category_form.html'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('products:category_list')
    template_name = 'product/category_confirm_delete.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'product/category_list.html'



class ManufacturerCreateView(CreateView):
    model = Manufacturer
    fields = '__all__'
    template_name = 'product/manufacturer_create.html'

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = '__all__'
    template_name = 'product/supplier_form.html'

class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    success_url = reverse_lazy('products:supplier_list')
    template_name = 'product/supplier_confirm_delete.html'

class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'product/manufacturer_list.html'

class TagCreateView(CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'product/tag_create.html'

class TagUpdateView(UpdateView):
    model = Tag
    fields = '__all__'
    template_name = 'product/tag_form.html'

class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('products:tag_list')
    template_name = 'product/tag_confirm_delete.html'

class TagListView(ListView):
    model = Tag
    template_name = 'product/tag_list.html'


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def product_search(request):
    search_term = request.GET.get("search", "").strip()



    products = Product.objects.filter(
                Q(name__icontains=search_term) |
                Q(description__icontains=search_term) |
                Q(category__name__icontains=search_term) |
                Q(tags__name__icontains=search_term) |
                Q(manufacturer__name__icontains=search_term)
            ).distinct()

    data = [
        {
            "name": product.name,
            "category_name": product.category.name,
            "manufacturer_name": product.manufacturer.name,
        }
        for product in products
    ]

    return JsonResponse(data, safe=False)

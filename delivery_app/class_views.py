from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Products, Categories, Reviews
from .forms import ReviewForm


# Productos

class ProductListView(ListView):
    model = Products
    template_name = "delivery_app/product_list.html"

class ProductDetailView(DetailView):
    model = Products
    template_name = "delivery_app/product_detail.html"

class ProductCreateView(CreateView):
    model = Products
    template_name = "delivery_app/product_create.html"
    success_url = reverse_lazy("ProductList")
    fields = ['title', 'price', 'category', 'image', 'description']

class ProductUpdateView(UpdateView):
    model = Products
    template_name = "delivery_app/product_edit.html"
    success_url = reverse_lazy("ProductList")
    fields = ['title', 'price', 'category_id', 'image', 'description']

class ProductDeleteView(DeleteView):
    model = Products
    template_name = "delivery_app/product_confirm_delete.html"
    success_url = reverse_lazy("ProductList")

# Productos filtrados por Categoría

class CategoryProductsListView(ListView):
    template_name = "delivery_app/category_products_list.html"

    def get_queryset(self):
        self.id = get_object_or_404(Categories, id=self.kwargs["category_id"])
        return Products.objects.filter(category_id=self.id)

# Categorías 

class CategoryListView(ListView):
    model = Categories
    template_name = "delivery_app/category_list.html"

class CategoryCreateView(CreateView):
    model = Categories
    template_name = "delivery_app/product_create.html"
    success_url = reverse_lazy("CategoryList")
    fields = ['title', 'image']

class CategoryUpdateView(UpdateView):
    model = Categories
    template_name = "delivery_app/product_edit.html"
    success_url = reverse_lazy("CategoryList")
    fields = ['title', 'image']

class CategoryDeleteView(DeleteView):
    model = Categories
    template_name = "delivery_app/category_confirm_delete.html"
    success_url = reverse_lazy("CategoryList")

# Reseñas

class ReviewCreateView(CreateView):
    form_class = ReviewForm

    template_name = "delivery_app/review_create.html"

    def form_valid(self, form):
        product_id = get_object_or_404(Products, id=self.kwargs['product_id'])
        author = self.request.user
        form.instance.product = product_id
        form.instance.author = author
        return super().form_valid(form)

    def get_success_url(self):
         return reverse_lazy("ProductDetail", kwargs={'pk': self.object.product_id})
 
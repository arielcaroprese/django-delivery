"""
URL configuration for django_delivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from delivery_app import views, class_views

urlpatterns = [
    path('', class_views.CategoryListView.as_view() , name='home'),
    path('sobre_mi/', views.about , name='about'),
]

# Productos

urlpatterns += [
    path('productos', class_views.ProductListView.as_view(), name='ProductList'),
    path('producto/<pk>/', class_views.ProductDetailView.as_view() , name='ProductDetail'),
    path('crear_producto/', class_views.ProductCreateView.as_view() , name='ProductCreate'),
    path('editar_producto/<pk>', class_views.ProductUpdateView.as_view() , name='ProductUpdate'),
    path('eliminar_producto/<pk>', class_views.ProductDeleteView.as_view() , name='ProductDelete'),
    path('buscar_productos/', views.product_search, name='buscar_productos')
]

# Categorías

urlpatterns += [
    path('categorias', class_views.CategoryListView.as_view(), name='CategoryList'),
    path("categoria/<category_id>/", class_views.CategoryProductsListView.as_view(), name='CategoryProductsList'),
    path('crear_categoria/', class_views.CategoryCreateView.as_view() , name='CategoryCreate'),
    path('editar_categoria/<pk>', class_views.CategoryUpdateView.as_view() , name='CategoryUpdate'),
    path('eliminar_categoria/<pk>', class_views.CategoryDeleteView.as_view() , name='CategoryDelete'),
]

# Reseñas

urlpatterns += [
    path("crear_resena/<product_id>", class_views.ReviewCreateView.as_view(), name='ReviewCreate'),
]
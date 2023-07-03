from django.shortcuts import render
from .models import Products, Categories
from .forms import ProductForm, CategoryForm, ProductSearch

def home(request):
    return render(request, "delivery_app/index.html")

def about(request):
    return render(request, "delivery_app/about.html")

    if request.method == 'POST':
             
        form = CategoryForm(request.POST)

        if form.is_valid():
            infoForm = form.cleaned_data
            category = Categories(title = infoForm["title"])
            category.save()
            return render(request, "delivery_app/index.html")
    else:
        form = CategoryForm()

    return render(request, "delivery_app/add_category.html", {"form": form})
        

    if request.method == 'POST':
             
        form = CouponForm(request.POST)

        if form.is_valid():
            infoForm = form.cleaned_data
            coupon = Coupons(coupon = infoForm["coupon"], discount = infoForm["discount"])
            coupon.save()
            return render(request, "delivery_app/index.html")
    
    else:
        form = CouponForm()

    return render(request, "delivery_app/add_coupon.html", {"form": form})

def product_search(request):
    if request.method =="POST":
         buscar_productos = ProductSearch(request.POST)

         if buscar_productos.is_valid():
             info = buscar_productos.cleaned_data
             productos = Products.objects.filter(title__icontains = info["title"])
             return render(request, "delivery_app/search_result.html", {"productos": productos})
    else:
        buscar_productos = ProductSearch()
        return render(request, "delivery_app/product_search.html", {"form": buscar_productos})
    
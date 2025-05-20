from django.shortcuts import render
from .models import Product
from django.core.cache import cache

def product_list(request):
    products = cache.get('all_products')

    if not products:
        products = Product.objects.all()
        cache.set('all_products', products, timeout=60)  # 60 seconds cache
        print("Data fetched from DB and cached.")
    else:
        print("Data fetched from cache.")

    return render(request, 'shop/product_list.html', {'products': products})

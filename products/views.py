from django.shortcuts import render, get_object_or_404
from .models import Product

# Created views here below.

def all_products(request):
    """ A view to show all products as well as include sorting and searching """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show seperate product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)



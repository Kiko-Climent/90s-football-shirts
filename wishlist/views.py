from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Wishlist
from products.models import Product
from profiles.models import UserProfile


def wishlist(request):
    wishlist_items = {}
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist_items})

def wishlist(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.get_or_create(user=request.user)[0]
        products_in_wishlist = wishlist.products.all()
        return render(request, 'wishlist/wishlist.html', {'products_in_wishlist': products_in_wishlist})
        #return render(request, 'wishlist.html', {'product_id': product_id})
    else:
        messages.info(request, f'Please log in to access to your wishlist')
        return render(request, 'accounts/login.html')

def add_to_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)

    if request.user.is_authenticated:
        print("User is authenticated")
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist.products.add(product)
        messages.success(request, f'Added {product.team} to your wishlist.')
        return redirect('product_detail', product_id=item_id)
    else:
        print("User is not authenticated")
        messages.info(request, f'Please log in to access to your wishlist')
        return redirect('login')
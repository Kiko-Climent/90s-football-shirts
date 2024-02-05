from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product
from profiles.models import UserProfile


@login_required
def wishlist(request):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    context = {
        'wishlist': wishlist
    }
    return render(request, 'wishlist/wishlist.html', context)

@login_required
def add_to_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.success(request, f'Added {product.team} to your wishlist.')
    return redirect('product_detail', product_id=item_id)

@login_required
def remove_from_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.remove(product)
    messages.success(request, f'Removed {product.team} from your wishlist.')
    
    return redirect('wishlist')


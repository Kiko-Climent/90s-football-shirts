from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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
"""
@login_required
def add_to_wishlist(request, item_id):
    product= get_object_or_404(Product, pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if wishlist.products.filter(pk=item_id).exists():
        messages.info(request, f'{product.team} is already in your wishlist.')
        return redirect('product_detail', product_id=item_id)
    else:
        wishlist.products.add(product)
        messages.success(request, f'Added {product.team} to your wishlist.')
        return redirect('product_detail', product_id=item_id)
"""
@login_required
def add_to_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    in_wishlist = wishlist.products.filter(pk=item_id).exists()
        #  OLD ONE!!!
    #if in_wishlist:
        # Product is already in the wishlist
    #    return JsonResponse({'in_wishlist': True})
    if in_wishlist:
        # Product is already in the wishlist
        return JsonResponse({'in_wishlist': True, 'success': False})

    wishlist.products.add(product)
    # Product added to the wishlist
    messages.success(request, f'Added {product.team} to your wishlist.')
    return JsonResponse({'in_wishlist': False})
    

@login_required
def remove_from_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.remove(product)
    messages.success(request, f'Removed {product.team} from your wishlist.')
    
    return redirect('wishlist')
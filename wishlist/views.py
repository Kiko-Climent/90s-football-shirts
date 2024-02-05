from django.shortcuts import render

from django.shortcuts import render

def wishlist(request):
    wishlist_items = {}
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist_items})

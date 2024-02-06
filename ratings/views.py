from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Rating
from products.models import Product
from profiles.models import UserProfile

from .forms import RatingForm

@login_required
def rate_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.product = product
            rating.user = request.user.userprofile
            rating.save()
            messages.success(request, 'Your rating has been added')
            return redirect ('product_detail', product_id=product_id)
        else:
            messages.error(request, 'Please select a value')
    else:
        form = RatingForm()
    
    return render(request, 'ratings/rate_product.html', {'form': form, 'product': product})

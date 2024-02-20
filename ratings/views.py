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
    user_profile = request.user.userprofile

    # Check if the user has already rated the product
    existing_rating = Rating.objects.filter(
        product=product, user=user_profile).first()

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            if existing_rating:
                # Update the existing rating
                existing_rating.value = form.cleaned_data['value']
                existing_rating.save()
                messages.success(request, 'Your rating has been updated')
            else:
                # Create a new rating
                rating = form.save(commit=False)
                rating.product = product
                rating.user = user_profile
                rating.save()
                messages.success(request, 'Your rating has been added')

            return redirect('product_detail', product_id=product_id)
        else:
            messages.error(request, 'Please select a value')
    else:
        form = RatingForm(instance=existing_rating)

    return render(
        request,
        'ratings/rate_product.html',
        {'form': form, 'product': product}
    )

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def purchase_view(request):
    shopping_cart = request.session.get('shopping_cart', {})
    if not shopping_cart:
        messages.error(request, 'Your shopping cart is empty')
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'purchase/purchase.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OZ8GyDgPKCOcRaNCflIxug6zGANzV3pYCVm4jp7Jczy9bcvD1dW4NFFMx8q6TTrCX0wq4eYmJ0HY2mTsJ3IXT1M00dVJzynkd',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

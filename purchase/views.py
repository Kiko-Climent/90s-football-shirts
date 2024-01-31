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
    }

    return render(request, template, context)

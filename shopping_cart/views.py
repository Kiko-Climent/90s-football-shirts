from django.shortcuts import render


def view_shopping_cart(request):
    return render(request, 'shopping_cart/shopping_cart.html')

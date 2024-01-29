from django.shortcuts import render, redirect, reverse, HttpResponse


def view_shopping_cart(request):
    return render(request, 'shopping_cart/shopping_cart.html')

def add_to_shopping_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_cart = request.session.get('shopping_cart', {})

    if size:
        if item_id in list(shopping_cart.keys()):
            if size in shopping_cart[item_id]['items_by_size'].keys():
                shopping_cart[item_id]['items_by_size'][size] += quantity
            else:
                shopping_cart[item_id]['items_by_size'][size] = quantity     
        else:
            shopping_cart[item_id] = {'items_by_size': {size: quantity}}
    else:       

        if item_id in list(shopping_cart.keys()):
            shopping_cart[item_id] += quantity
        else:
            shopping_cart[item_id] = quantity

    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)

def update_shopping_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_cart = request.session.get('shopping_cart', {})

    if size:
        if quantity > 0:
            shopping_cart[item_id]['items_by_size'][size] = quantity
        else:
            del shopping_cart[item_id]['items_by_size'][size]
            if not shopping_cart[item_id]['items_by_size']:
                shopping_cart.pop(item_id)
    else:       

        if quantity > 0:
            shopping_cart[item_id] = quantity
        else:
            shopping_cart.pop(item_id)

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('shopping_cart'))

def remove_from_shopping_cart(request, item_id):

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopping_cart = request.session.get('shopping_cart', {})

        if size:
            del shopping_cart[item_id]['items_by_size'][size]
            if not shopping_cart[item_id]['items_by_size']:
                shopping_cart.pop(item_id)
        else:
            shopping_cart.pop(item_id)

        request.session['shopping_cart'] = shopping_cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
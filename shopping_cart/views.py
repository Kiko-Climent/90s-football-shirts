from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product


#def view_shopping_cart(request):
#    return render(request, 'shopping_cart/shopping_cart.html')


def view_shopping_cart(request):
    shopping_cart = request.session.get('shopping_cart', {})
    return render(request, 'shopping_cart/shopping_cart.html', {'shopping_cart': shopping_cart})


def add_to_shopping_cart(request, item_id):

    print(request.POST)

    product = get_object_or_404(Product, pk=item_id)
    #quantity = int(request.POST.get('quantity')) OLD ONE
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_cart = request.session.get('shopping_cart', {})

    if size:
        if item_id in list(shopping_cart.keys()):
            if size in shopping_cart[item_id]['items_by_size'].keys():
                shopping_cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.team} quantity to {shopping_cart[item_id]["items_by_size"][size]}')
                
            else:
                shopping_cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.team} to your cart')    
        else:
            shopping_cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.team} to your cart')
    else:       

        if item_id in list(shopping_cart.keys()):
            shopping_cart[item_id] += quantity
            messages.success(request, f'Updated {product.team} quantity to {shopping_cart[item_id]}')
        else:
            shopping_cart[item_id] = quantity
            messages.success(request, f'Added {product.team} to your cart')
    
    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)


def update_shopping_cart(request, item_id,):
    """
    if set size to '' and no ['items_by_size'] gets same result. NEEDS CHECK!!
    """
    product = get_object_or_404(Product, pk=item_id)
    #quantity = int(request.POST.get('quantity')) OLD ONE
    quantity = int(request.POST.get('quantity', 1))
    size = None
    #size = ''
    #size = {'XS', 'S', 'M', 'L', 'XL'}
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_cart = request.session.get('shopping_cart', {})

    if size:
        if quantity > 0:
            #shopping_cart[item_id] = sum(shopping_cart[item_id]['items_by_size'].values())  # Update main quantity
            shopping_cart[item_id]['items_by_size'][size] = quantity
            #shopping_cart[item_id][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.team} quantity to {shopping_cart[item_id]["items_by_size"][size]}')
        else:
            del shopping_cart[item_id]['items_by_size'][size]
            if not shopping_cart[item_id]['items_by_size']:
                shopping_cart.pop(item_id)   
            messages.success(request, f'Remove size {size.upper()} {product.team} from your cart')
    else:       

        if quantity > 0:
            shopping_cart[item_id] = quantity   
            messages.success(request, f'Updated {product.team} quantity to {shopping_cart[item_id]}')
        else:
            shopping_cart.pop(item_id)  
            messages.success(request, f'Removed {product.team} from your cart')

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('shopping_cart'))


def remove_from_shopping_cart(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopping_cart = request.session.get('shopping_cart', {})

        if size:
            del shopping_cart[item_id]['items_by_size'][size]
            if not shopping_cart[item_id]['items_by_size']:
                shopping_cart.pop(item_id)
            messages.success(request, f'Remove size {size.upper()} {product.team} from your cart')
        else:
            shopping_cart.pop(item_id)
            messages.success(request, f'Removed {product.team} from your cart')

        request.session['shopping_cart'] = shopping_cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request,f'Error removing item: {e}')
        return HttpResponse(status=500)


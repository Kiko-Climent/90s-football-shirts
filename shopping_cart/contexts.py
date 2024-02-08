from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

"""
def shopping_cart_contents(request):

    shopping_cart_items = []
    total = 0
    product_count = 0
    shopping_cart = request.session.get('shopping_cart', {})

    for item_id, item_data in shopping_cart.items():
        if isinstance(item_data, int):
            print(f'context -> item_id == {item_id}')
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            shopping_cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                shopping_cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'size': size,
            })

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0
    
    grand_total = shipping + total
    
    context = {
        'shopping_cart_items': shopping_cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
"""    

#    Context to implement the discount:

def shopping_cart_contents(request):

    shopping_cart_items = []
    total = 0
    product_count = 0
    quantity = 0
    #discount_percentage = settings.DISCOUNT_PERCENTAGE
    shopping_cart = request.session.get('shopping_cart', {})

    cheapest_item_price = float('inf')
    cheapest_item = None
    discount_applied = False

    for item_id, item_data in shopping_cart.items():
        if isinstance(item_data, int):
            #print(f'context -> item_id == {item_id}')
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            shopping_cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

            if len(shopping_cart_items) > 1 and product.price < cheapest_item_price:
                cheapest_item_price = product.price
                cheapest_item = {
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                }

        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                shopping_cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'size': size,
            })

            if len(shopping_cart_items) > 1 and product.price < cheapest_item_price:
                cheapest_item_price = product.price
                cheapest_item = {
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                }

    if len(shopping_cart_items) > 1 and 'cheapest_item' in locals() and not discount_applied:
        cheapest_item['discounted_price'] = cheapest_item_price * Decimal(0.5)
        cheapest_item['discounted'] = True
        total -= cheapest_item_price * cheapest_item['quantity']
        total += cheapest_item['discounted_price'] * cheapest_item['quantity']
        #total += cheapest_item['discounted_price']
        discount_applied = True

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0
    
    grand_total = shipping + total

    if cheapest_item is not None:
        context = {
            'shopping_cart_items': shopping_cart_items,
            'cheapest_item': cheapest_item,
            'total': total,
            'product_count': product_count,
            'shipping': shipping,
            'free_shipping_delta': free_shipping_delta,
            'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
            'grand_total': grand_total,
        }
    else:
        context = {
            'shopping_cart_items': shopping_cart_items,
            'total': total,
            'product_count': product_count,
            'shipping': shipping,
            'free_shipping_delta': free_shipping_delta,
            'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
            'grand_total': grand_total,
        }

    return context

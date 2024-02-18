from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


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

    """ Discount calculator """
    discount = 0
    discounted_total = total
    
    if total > settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
        discounted_total = total  # Initialize discounted total with the original total
    
        if total > settings.DISCOUNT_THRESHOLD:
            discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
            discounted_total -= discount

    if discounted_total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = discounted_total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - discounted_total
    else:
        shipping = 0
        free_shipping_delta = 0
    
    grand_total = shipping + discounted_total

    context = {
        'shopping_cart_items': shopping_cart_items,
        'total': total,
        'discounted_total': discounted_total,
        'discount': discount,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

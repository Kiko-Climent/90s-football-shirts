from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm
from ratings.forms import RatingForm
from wishlist.models import Wishlist


def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    brands = None
    product_rating = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            print(categories)
            category = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__in=brands)
            print(brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please, enter a search criteria")
                return redirect(reverse('products'))

            queries = Q(
                    team__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            product_ratings = []
            # Fetch ratings for each product in the loop
            for product in products:
                product_rating = product.ratings.aggregate(
                    Avg('value'))['value__avg']
                # Include product_rating in the context for each product
                product.product_rating = product_rating
                # Append the rating to the list
                product_ratings.append(product_rating)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_brands': brands,
        'product_rating': product_rating,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    rating_form = RatingForm()

    if request.method == 'POST' and request.user.is_authenticated:
        # Handle form submission
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            new_rating = rating_form.save(commit=False)
            new_rating.product = product
            new_rating.user = request.user
            new_rating.save()

    # Fetch the updated average rating
    user_product_rating = product.ratings.aggregate(Avg('value'))['value__avg']

    # Check if there's an admin or default rating
    admin_rating = float(
        product.rating) if product.rating is not None else None

    """
    Consider both user ratings and admin/default rating
    when calculating the average
    """
    if user_product_rating is not None:
        total_ratings = product.ratings.count()  # Count of user ratings
        total_rating_value = total_ratings * user_product_rating

        if admin_rating is not None:
            total_ratings += 1  # Include admin rating in the count
            total_rating_value += admin_rating

        average_rating = total_rating_value / total_ratings
    else:
        """
        Display admin/default rating if no user rating is available
        """
        average_rating = admin_rating

    # Check if the product is in the wishlist
    product_in_wishlist = False
    if request.user.is_authenticated:
        product_in_wishlist = Wishlist.objects.filter(
                user=request.user, products=product).exists()

    context = {
        'product': product,
        'rating_form': rating_form,
        'product_rating': average_rating,
        'product_in_wishlist': product_in_wishlist,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Im afraid only site owner can proceed with that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product succesfully added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Error by adding the product. \
                        Make sure you enter a valid form.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Update an existing product"""

    if not request.user.is_superuser:
        messages.error(
            request, 'Im afraid only site owner can proceed with that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product succesfully updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Error by updating this product, \
                        please check the form')
    else:
        form = ProductForm(instance=product)
        messages.info(
                request, f'You are about to edit \
                        the product: { product.team }')
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete an existing product from the database """

    if not request.user.is_superuser:
        messages.error(
            request, 'Im afraid only site owner can proceed with that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

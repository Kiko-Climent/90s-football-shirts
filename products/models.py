from django.db import models
from django.db.models import Avg

from profiles.models import UserProfile



class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    team = models.CharField(max_length=254)
    season = models.CharField(max_length=254)
    brand = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=True, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    users_wishlist = models.ManyToManyField(UserProfile, related_name='wishlist_products', blank=True)

    def __str__(self):
        return self.team
    
    def average_rating(self):
        from ratings.models import Rating  # Importing locally to avoid circular import
        avg_rating = Rating.objects.filter(product=self).aggregate(Avg('value'))['value__avg']
        return avg_rating if avg_rating is not None else 0
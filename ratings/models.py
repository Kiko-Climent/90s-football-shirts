from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product
from profiles.models import UserProfile

class Rating(models.Model):
    VALUE_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=VALUE_CHOICES
    )

    def __str__(self):
        return f'{self.user.username} - {self.product.team}'


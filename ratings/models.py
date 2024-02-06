from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product
from profiles.models import UserProfile

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.user.username} - {self.product.team}'

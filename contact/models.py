from django.db import models
from products.models import Product

class Inquiry(models.Model):
    INQUIRY_CHOICES = [
        ('GENERAL', 'General Inquiry'),
        ('PRODUCT', 'Product Inquiry'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=False)
    subject_type = models.CharField(
        max_length=10, choices=INQUIRY_CHOICES,
        default='GENERAL', blank=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    message = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject_type} - {self.product}" if self.subject_type == 'PRODUCT' else self.subject_type

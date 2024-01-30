from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderDetail

@receiver(post_save, sender=OrderDetail)
def update_on_save(sender, instance, receiver, **kwargs):
    instance.order.update_total()

@receiver(post_delete, sender=OrderDetail)
def update_on_save(sender, instance, receiver, **kwargs):
    instance.order.update_total()
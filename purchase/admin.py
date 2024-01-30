from django.contrib import admin
from .models import Order, OrderDetail


class OrderDetailAdminInline(admin.TabularInline):
    model = OrderDetail
    readonly_fields = ('orderdetail_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderDetailAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'shipping_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'shipping_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'shipping_cost',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
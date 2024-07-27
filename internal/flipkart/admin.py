from django.contrib import admin
from flipkart.models import Order


class OrderModel(admin.ModelAdmin):
    list_display = ('order_date', 'order_id', 'tracking_id',
                    'shipment_type', 'delivery_status', 'final_settlement')

    list_filter = ('shipment_type', 'delivery_status')


admin.site.register(Order, OrderModel)

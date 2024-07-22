from django.contrib import admin
from flipkart.models import OrderList


class OrderListModel(admin.ModelAdmin):
    list_display = ('order_date', 'order_id', 'tracking_id',
                    'shipment_type', 'delivery_status', 'total_disbursement_amount')

    list_filter = ('shipment_type', 'delivery_status')


admin.site.register(OrderList, OrderListModel)

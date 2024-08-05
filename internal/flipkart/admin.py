from django.contrib import admin
from flipkart.models import Order


class ReadOnlyVariableFilter(admin.SimpleListFilter):
    title = 'Pending'
    parameter_name = 'pending'

    def lookups(self, request, model_admin):
        # Define the filter options
        return [
            ('YES', 'YES'),
            ('NO', 'NO'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'YES':
            # Filter queryset based on the property value
            return queryset.filter(id__in=[obj.id for obj in queryset if obj.pending == 'YES'])
        if self.value() == 'NO':
            # Define other filter logic here
            return queryset.filter(id__in=[obj.id for obj in queryset if obj.pending == 'NO'])
        return queryset


class OrderModel(admin.ModelAdmin):
    list_display = ('order_date', 'order_id', 'tracking_id',
                    'shipment_type', 'delivery_status', 'final_settlement', 'pending')

    list_filter = (ReadOnlyVariableFilter, 'shipment_type', 'delivery_status')


admin.site.register(Order, OrderModel)

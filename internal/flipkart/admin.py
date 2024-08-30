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


def mark_as_delivered(modeladmin, request, queryset):
    updated_count = queryset.update(delivery_status='DELIVERED')
    modeladmin.message_user(
        request, f"{updated_count} orders marked as delivered.")
    
def mark_as_courier_return(modeladmin, request, queryset):
    updated_count = queryset.update(shipment_type='COURIER')
    modeladmin.message_user(
        request, f"{updated_count} orders marked as Courier Return.")
    
def mark_as_customer_return(modeladmin, request, queryset):
    updated_count = queryset.update(shipment_type='CUSTOMER')
    modeladmin.message_user(
        request, f"{updated_count} orders marked as Customer Return.")


mark_as_delivered.short_description = "Mark selected orders as Delivered"
mark_as_courier_return.short_description = "Mark selected orders as Courier Return"
mark_as_customer_return.short_description = "Mark selected orders as Customer Return"


class OrderModel(admin.ModelAdmin):
    list_display = ('order_date', 'order_id', 'tracking_id',
                    'shipment_type', 'delivery_status', 'final_settlement', 'pending')

    search_fields = ("order_id", "tracking_id")
    actions = [mark_as_delivered, mark_as_courier_return, mark_as_customer_return]
    ordering = ('-order_date',)

    list_filter = (ReadOnlyVariableFilter, 'shipment_type', 'delivery_status')


admin.site.register(Order, OrderModel)

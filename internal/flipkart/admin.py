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


mark_as_delivered.short_description = "Mark selected orders as Delivered"


class OrderModel(admin.ModelAdmin):
    list_display = ('order_date', 'order_id', 'tracking_id',
                    'shipment_type', 'delivery_status', 'final_settlement', 'pending')

    search_fields = ("order_id", "tracking_id")
    actions = [mark_as_delivered]
    ordering = ('-order_date',)

    list_filter = (ReadOnlyVariableFilter, 'shipment_type', 'delivery_status')


admin.site.register(Order, OrderModel)

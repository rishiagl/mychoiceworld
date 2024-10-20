from django.contrib import admin
from .models import PurchaseInvoice, PurchaseInvoiceItem
from register.models import Product


class PurchaseInvoiceItemInline(admin.TabularInline):
    model = PurchaseInvoiceItem
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.order_by('brand__name', 'category__name', 'model')  # Order products by name
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PurchaseInvoiceAdmin(admin.ModelAdmin):
    inlines = [PurchaseInvoiceItemInline]
    list_display = ('invoice_date', 'organisation',
                    'account', 'invoice_no', 'total_amount')
    search_fields = ("invoice_no",)
    ordering = ('-invoice_date',)
    list_filter = ('organisation', 'invoice_date')

    def total_amount(self, obj):
        return round(obj.total_amount)


admin.site.register(PurchaseInvoice, PurchaseInvoiceAdmin)

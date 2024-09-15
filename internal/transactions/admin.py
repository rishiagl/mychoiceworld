from django.contrib import admin
from .models import PurchaseInvoice, PurchaseInvoiceItem


class PurchaseInvoiceItemInline(admin.TabularInline):
    model = PurchaseInvoiceItem
    extra = 1


class PurchaseInvoiceAdmin(admin.ModelAdmin):
    inlines = [PurchaseInvoiceItemInline]
    list_display = ('invoice_date', 'organisation', 'account', 'invoice_no', 'total_amount')
    search_fields = ("invoice_no",)
    ordering= ('-invoice_date',)
    list_filter = ('organisation',)


admin.site.register(PurchaseInvoice, PurchaseInvoiceAdmin)

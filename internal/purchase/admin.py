from django.contrib import admin
from .models import Invoice, InvoiceItem


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ('invoice_date', 'organisation', 'account', 'invoice_no', 'total_amount')
    search_fields = ("invoice_no",)
    ordering= ('-invoice_date',)
    list_filter = ('organisation',)


admin.site.register(Invoice, InvoiceAdmin)


class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(InvoiceItem, InvoiceItemAdmin)

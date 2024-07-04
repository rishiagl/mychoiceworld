from django.contrib import admin

from inventory.models import Warehouse, StockItem


class WarehouseInline(admin.TabularInline):
    model = StockItem
    extra = 1


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'organisation', 'phone_no')
    inlines = [WarehouseInline]


admin.site.register(Warehouse, WarehouseAdmin)


class StockItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'qty')
    list_filter = ["warehouse", 'product__brand', 'product__category']
    search_fields = ("product__name__startswith",)


admin.site.register(StockItem, StockItemAdmin)

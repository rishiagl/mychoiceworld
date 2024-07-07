from django.contrib import admin

from inventory.models import Warehouse, StockItem, StockItemChangeLog


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


class StockItemChangeLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'stock_item_product_name',
                    'stock_item_warehouse', 'stock_item_qty')
    list_filter = ('stock_item__warehouse', 'date', 'stock_item__product')

    def stock_item_product_name(self, obj):
        return obj.stock_item.product.name

    def stock_item_warehouse(self, obj):
        return obj.stock_item.warehouse.name

    def stock_item_qty(self, obj):
        return obj.stock_item.qty


admin.site.register(StockItemChangeLog, StockItemChangeLogAdmin)

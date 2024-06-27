from django.contrib import admin

from .models import Brand, Category, Product, GstClassification

from django.utils.text import slugify

admin.site.site_header = "CERMS Administration Panel"


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortName')


admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortName')


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'brand', 'category')
    readonly_fields = ('name',)

    def get_readonly_fields(self, request, obj=None):
        if obj is None:  # This is an add operation
            return ()
        return self.readonly_fields


admin.site.register(Product, ProductAdmin)


class GstClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'type', 'rate')

    def name(self, obj):
        return obj


admin.site.register(GstClassification, GstClassificationAdmin)

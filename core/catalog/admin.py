from django.contrib import admin, messages

from .models import Brand, Category, Product, GstClassification


admin.site.site_header = "My Choice Enterprise Resource Management"
admin.site.site_title = "My Choice"
admin.site.index_title = "Administration Panel"


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ("name__startswith",)


admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ("name__startswith",)


admin.site.register(Category, CategoryAdmin)


def Download_QR_Code(modeladmin, request, queryset):
    pass


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'brand', 'category', 'gst_classification')
    list_filter = ["brand", "category"]
    search_fields = ("model__startswith",)
    actions = [Download_QR_Code]


admin.site.register(Product, ProductAdmin)


class GstClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'type', 'rate')

    def name(self, obj):
        return obj


admin.site.register(GstClassification, GstClassificationAdmin)

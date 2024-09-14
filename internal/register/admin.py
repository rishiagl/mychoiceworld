from django.contrib import admin, messages

from .models import Brand, Category, Product, IndianState, Account, Organisation


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
    list_display = ('name', 'model', 'brand', 'category')
    list_filter = ["brand", "category", "is_active"]
    search_fields = ("model__startswith",)
    actions = [Download_QR_Code]

admin.site.register(Product, ProductAdmin)

class IndianStateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)

admin.site.register(IndianState, IndianStateAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Account, AccountAdmin)

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Organisation, OrganisationAdmin)

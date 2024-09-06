from django.contrib import admin
from retail.models import Merchant, ProductCategory, FinanceCompany, SingleProductInvoiceSeries, SingleProductInvoice

class MerchantModel(admin.ModelAdmin):
    list_display = ('name', 'email', 'primary_phone_no')

    search_fields = ("name",)

admin.site.register(Merchant, MerchantModel)

class ProductCategoryModel(admin.ModelAdmin):
    list_display = ('name', 'hsn_no', 'tax_rate')
    search_fields = ('name', 'hsn_no', 'tax_rate')
    
admin.site.register(ProductCategory, ProductCategoryModel)

class FinanceCompanyModel(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(FinanceCompany, FinanceCompanyModel)

class SingleProductInvoiceSeriesModel(admin.ModelAdmin):
    list_display = ('name', 'invoice_prefix', 'invoice_start_no', 'invoice_end_no')

admin.site.register(SingleProductInvoiceSeries, SingleProductInvoiceSeriesModel)

class SingleProductInvoiceModel(admin.ModelAdmin):
    list_display = ('invoice_date', 'invoice_no', "merchant", "customer_name", "customer_phone_number", "product_name", "product_category", "product_amount", "amount_due")
    
    search_fields = ("invoice_no", "customer_name", "customer_phone_number")
    
admin.site.register(SingleProductInvoice, SingleProductInvoiceModel)
    
    


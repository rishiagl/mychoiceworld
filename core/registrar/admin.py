from django.contrib import admin
from django.utils.html import format_html

from .models import Organisation, Customer, Financer


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'legal_name', 'gstn', 'email', 'web_URL')

    def web_URL(self, obj):
        return format_html('<a href="{}">{}</a>', obj.website, obj.website)


admin.site.register(Organisation, OrganisationAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'primary_phone_no', 'city')


admin.site.register(Customer, CustomerAdmin)

# class FinancerAdmin(admin.ModelAdmin):
#     list_display = ('name')


# admin.site.register(Financer, FinancerAdmin)

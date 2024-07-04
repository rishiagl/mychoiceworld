from django.contrib import admin
from django.utils.html import format_html

from .models import Organisation, Account


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'legal_name', 'gstn', 'email', 'web_URL')

    def web_URL(self, obj):
        return format_html('<a href="{}">{}</a>', obj.website, obj.website)


admin.site.register(Organisation, OrganisationAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_no', 'email')


admin.site.register(Account, AccountAdmin)

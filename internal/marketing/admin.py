from django.contrib import admin
from marketing.models import CallbackRequests

# Register your models here.


class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'last_updated', 'customer_name',
                    'phone_no', 'remark', 'is_starred', 'is_closed', )


admin.site.register(CallbackRequests, CallbackRequestAdmin)

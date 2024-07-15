from rest_framework import serializers
from marketing.models import CallbackRequests


class CallbackRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackRequests
        fields = ['created_on', 'customer_name', 'phone_no',
                  'remark', 'is_starred', 'is_closed', 'last_updated']

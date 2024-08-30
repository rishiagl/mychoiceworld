from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.timezone import now

DeliveryStatus = (
    ('ON_THE_WAY', 'ON_THE_WAY'),
    ('DELIVERED', 'DELIVERED'),
    ('RETURNED', 'RETURNED'),
)

ShipmentType = (
    ('NORMAL', 'No Return'),
    ('COURIER', 'Courier Return'),
    ('CUSTOMER', 'Customer Return'),
)


class Order(models.Model):
    order_date = models.DateField(default=now)
    order_id = models.CharField(max_length=30, blank=False, unique=True)
    product = models.CharField(max_length=100, blank=True)
    buyer_name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    tracking_id = models.CharField(max_length=30, blank=False, unique=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_status = models.CharField(
        max_length=100, choices=DeliveryStatus, blank=False, default='ON_THE_WAY')
    shipment_type = models.CharField(
        max_length=100, choices=ShipmentType, blank=False, default='NORMAL')
    final_settlement = models.IntegerField(blank=True, default=0)
    
    def __str__(self) -> str:
        return self.order_id
    
    @property
    def pending(self):
        if self.shipment_type == 'COURIER':
            if self.delivery_status == 'RETURNED':
                return "NO"
            else:
                return "YES"
        else:
            if self.delivery_status == "ON_THE_WAY" or self.final_settlement == 0:
                return "YES"
            else:
                return "NO"
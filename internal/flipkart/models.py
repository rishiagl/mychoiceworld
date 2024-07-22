from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

DeliveryStatus = (
    ('ON_THE_WAY', 'ON_THE_WAY'),
    ('DELIVERED', 'DELIVERED'),
    ('RETURNED', 'RETURNED'),
)

ShipmentType = (
    ('NORMAL', 'No Return'),
    ('COURIER', 'Courier Return'),
    ('CUsTOMER', 'Customer Return'),
)


class OrderList(models.Model):
    order_date = models.DateField()
    order_id = models.CharField(max_length=23, blank=False, unique=True)
    product = models.CharField(max_length=100, blank=True)
    buyer_name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    tracking_id = models.CharField(max_length=20, blank=False, unique=True)
    delivery_status = models.CharField(
        max_length=100, choices=DeliveryStatus, blank=False, default='ON_THE_WAY')
    shipment_type = models.CharField(
        max_length=100, choices=ShipmentType, blank=False, default='NORMAL')
    total_disbursement_amount = models.IntegerField(blank=True, default=0)

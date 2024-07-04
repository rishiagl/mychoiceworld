from django.db import models
from catalog.models import Product
from registrar.models import Organisation
from django.utils.text import slugify

StateChoice = (
    ('JHARKHAND', 'JHARKHAND'),
    ('WEST BENGAL', 'WEST BENGAL'),
    ('BIHAR', 'BIHAR'),
    ('ODISHA', 'ODISHA'),
    ('CHATTISGARH', 'CHATTISHGARH'),
)


class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.RESTRICT)
    phone_no = models.CharField(max_length=10, blank=False, unique=True)
    address_line_1 = models.CharField(max_length=50, blank=False)
    address_line_2 = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=20, blank=False)
    state = models.CharField(
        max_length=100, choices=StateChoice, blank=False, default='JHARKHAND')
    pincode = models.CharField(max_length=6, blank=False)

    def save(self, *args, **kwargs):
        self.name = slugify(self.name).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class StockItem(models.Model):
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    qty = models.IntegerField(blank=False)

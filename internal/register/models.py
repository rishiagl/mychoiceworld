from django.db import models
from django.forms import ValidationError


def validate_Code(value):
    if not value.isdigit():
        raise ValidationError(f"{value} is not an integer.")


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    Type_Choices = (
        ('HSN', 'Goods'),
        ('SAC', 'Services'),
    )

    Rate_Choices = (
        (6, '6%'),
        (12, '12%'),
        (18, '18%'),
        (28, '28%'),
    )
    type = models.CharField(
        max_length=10, choices=Type_Choices, default='HSN')
    model = models.CharField(max_length=100, blank=True, editable=True)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    code = models.CharField(max_length=8,
                            validators=[validate_Code])
    rate = models.IntegerField(choices=Rate_Choices, default='18')
    is_active = models.BooleanField(default=True)

    @property
    def name(self, *args, **kwargs):
        return self.brand.name + '-' + self.category.name + '-' + self.model

    def save(self, *args, **kwargs):
        self.model = self.model.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class IndianState(models.Model):
    name = models.CharField(max_length=25, unique=True)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)


class Account(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Organisation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)
    primary_phone_no = models.CharField(
        max_length=10, blank=False, unique=True)
    secondary_phone_no = models.CharField(max_length=10, blank=True)
    address_line_1 = models.CharField(max_length=50, blank=False)
    address_line_2 = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=20, blank=False)
    state = models.ForeignKey(IndianState, on_delete=models.RESTRICT)
    pincode = models.CharField(max_length=6, blank=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.address_line_1 = self.address_line_1.upper()
        self.address_line_2 = self.address_line_2.upper()
        self.city = self.city.upper()
        super().save(*args, **kwargs)


class ProductSerialNo(models.Model):
    number = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    is_validated = models.BooleanField(default=False)

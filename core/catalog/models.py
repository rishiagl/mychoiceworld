from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify


def validate_Code(value):
    if not value.isdigit():
        raise ValidationError(f"{value} is not an integer.")


class GstClassification(models.Model):
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

    code = models.CharField(max_length=8, unique=True,
                            validators=[validate_Code])
    description = models.TextField(max_length=100, blank=True)
    rate = models.IntegerField(choices=Rate_Choices, default='18')

    def __str__(self):
        return self.type + '-' + self.code + '-' + str(self.rate)


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=5, unique=True, editable=True)

    def save(self, *args, **kwargs):
        self.name = slugify(self.name).upper()
        self.short_name = self.short_name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=5, unique=True)

    def save(self, *args, **kwargs):
        self.name = slugify(self.name).upper()
        self.short_name = self.short_name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    model = models.CharField(max_length=100, blank=True, editable=True)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    gst_classification = models.ForeignKey(
        GstClassification, on_delete=models.RESTRICT)
    is_active = models.BooleanField(default=True)

    def name(self, *args, **kwargs):
        return self.brand.short_name + '-' + self.category.short_name + '-' + self.model

    def save(self, *args, **kwargs):
        self.model = slugify(self.model).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name()

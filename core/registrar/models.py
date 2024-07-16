from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

StateChoice = (
    ('JHARKHAND', 'JHARKHAND'),
    ('WEST BENGAL', 'WEST BENGAL'),
    ('BIHAR', 'BIHAR'),
    ('ODISHA', 'ODISHA'),
    ('CHATTISGARH', 'CHATTISHGARH'),
)


class Organisation(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    code = models.CharField(max_length=3, unique=True, blank=False)
    legal_name = models.CharField(max_length=100)
    gstn = models.CharField(max_length=15, unique=True, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=False, unique=True)
    phoneNo = models.CharField(max_length=10, blank=False, unique=True)
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


class Customer(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=True)
    primary_phone_no = models.CharField(
        max_length=10, blank=False, unique=True)
    secondary_phone_no = models.CharField(max_length=10, blank=True)
    address_line_1 = models.CharField(max_length=50, blank=False)
    address_line_2 = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=20, blank=False)
    state = models.CharField(
        max_length=100, choices=StateChoice, blank=False, default='JHARKHAND')
    pincode = models.CharField(max_length=6, blank=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        user = User.objects.create_user(
            username=self.primary_phone_no, email=self.primary_phone_no, password=self.primary_phone_no).save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Financer(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def save(self, *args, **kwargs):
        self.name = slugify(self.name).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    organisation = models.ForeignKey(
        Organisation, blank=False, on_delete=models.RESTRICT)
    bank_name = models.CharField(max_length=20, blank=False)
    account_no = models.CharField(max_length=20, blank=False)
    ifsc_code = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.bank_name + '-' + self.account_no


class CashAccount(models.Model):
    organisation = models.ForeignKey(
        Organisation, blank=False, on_delete=models.RESTRICT)
    name = models.CharField(max_length=30, blank=False, unique=True)

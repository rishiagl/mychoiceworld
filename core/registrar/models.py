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
    address_line_1 = models.CharField(max_length=20, blank=False)
    address_line_2 = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=20, blank=False)
    state = models.CharField(
        max_length=100, choices=StateChoice, blank=False, default='JHARKHAND')
    pincode = models.CharField(max_length=6, blank=False)

    def save(self, *args, **kwargs):
        self.name = slugify(self.name).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False, unique=True)
    phone_no = models.CharField(max_length=10, blank=False)
    organisations = models.ManyToManyField(Organisation)

    def save(self, *args, **kwargs):
        user = User.objects.create_user(
            username=self.email, email=self.email, password=self.email).save()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

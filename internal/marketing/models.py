from typing import Iterable
from django.db import models
import datetime

# Create your models here.


class CallbackRequests(models.Model):
    created_on = models.DateTimeField(default=datetime.datetime.now())
    customer_name = models.CharField(max_length=50, default="None")
    phone_no = models.CharField(max_length=10)
    # Remark from the organisation
    remark = models.TextField(max_length=200, blank=True)
    # A call marked for re-visit
    is_starred = models.BooleanField(default=False)
    # when the call closes
    is_closed = models.BooleanField(default=False)
    last_updated = models.DateTimeField(default=datetime.datetime.now())

    def save(self, *args, **kwargs):
        self.last_updated = datetime.datetime.now()
        super().save(*args, **kwargs)

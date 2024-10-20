from django.db import models
from register.models import Account, Organisation, Product
from django.utils.timezone import now

# Create your models here.


class PurchaseInvoice(models.Model):
    invoice_date = models.DateField(default=now)
    invoice_no = models.CharField(
        max_length=20, unique=True, blank=False, null=False)
    organisation = models.ForeignKey(Organisation, on_delete=models.RESTRICT)
    account = models.ForeignKey(Account, on_delete=models.RESTRICT)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.invoice_no

    @property
    def total_taxable_value(self):
        invoiceItems = PurchaseInvoiceItem.objects.filter(invoice=self)
        x = 0
        for invoiceItem in invoiceItems:
            x = x + (invoiceItem.taxable_value * invoiceItem.qty)

        return round(x, 2)

    @property
    def total_cgst(self):
        invoiceItems = PurchaseInvoiceItem.objects.filter(invoice=self)
        x = 0
        for invoiceItem in invoiceItems:
            x = x + (invoiceItem.cgst * invoiceItem.qty)

        return round(x, 2)

    @property
    def total_sgst(self):
        invoiceItems = PurchaseInvoiceItem.objects.filter(invoice=self)
        x = 0
        for invoiceItem in invoiceItems:
            x = x + (invoiceItem.sgst * invoiceItem.qty)

        return round(x, 2)

    @property
    def total_igst(self):
        invoiceItems = PurchaseInvoiceItem.objects.filter(invoice=self)
        x = 0
        for invoiceItem in invoiceItems:
            x = x + (invoiceItem.igst * invoiceItem.qty)

        return round(x, 2)

    @property
    def total_amount(self):
        return round(self.total_taxable_value + self.total_cgst + self.total_sgst + self.total_igst, 2)


class PurchaseInvoiceItem(models.Model):
    invoice = models.ForeignKey(PurchaseInvoice, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    qty = models.IntegerField(default=0)
    taxable_value = models.FloatField(blank=False, null=False)
    cgst = models.FloatField(blank=False, null=False)
    sgst = models.FloatField(blank=False, null=False)
    igst = models.FloatField(blank=False, null=False)

    def __str__(self) -> str:
        return self.invoice.invoice_no + '_' + self.product.name

    @property
    def rate(self):
        return round(self.taxable_value + self.cgst + self.sgst + self.igst, 2)

    @property
    def total_amount(self):
        return round(self.rate * self.qty, 2)

    @property
    def date(self):
        return self.invoice.invoice_date

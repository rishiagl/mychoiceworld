from django.db import models
from django.utils.timezone import now

StateChoice = (
    ('JHARKHAND', 'JHARKHAND'),
    ('WEST BENGAL', 'WEST BENGAL'),
    ('BIHAR', 'BIHAR'),
    ('ODISHA', 'ODISHA'),
    ('CHATTISGARH', 'CHATTISHGARH'),
)

class Merchant(models.Model):
    name = models.CharField(max_length=50, unique=True)
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
    
    def __str__(self) -> str:
        return self.name
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    hsn_no = models.CharField(max_length=8, blank=False)
    tax_rate = models.IntegerField(blank=False)
    
    def __str__(self) -> str:
        return self.name + "_" + str(self.tax_rate)
    
class FinanceCompany(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self) -> str:
        return self.name

class SingleProductInvoiceSeries(models.Model):
    name = models.CharField(max_length=10, unique=True)
    invoice_prefix = models.CharField(max_length=10, unique=True)
    invoice_start_no = models.IntegerField()
    invoice_end_no = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class SingleProductInvoice(models.Model):
    series = models.ForeignKey(SingleProductInvoiceSeries, on_delete=models.RESTRICT)
    invoice_date = models.DateField(default=now)
    invoice_no = models.CharField(max_length=20, unique=True, blank=False, null=False)
    merchant = models.ForeignKey(Merchant, on_delete=models.RESTRICT)
    customer_phone_number = models.CharField(max_length=10, blank=False)
    customer_name = models.CharField(max_length=50, blank=False)
    customer_address_line_1 = models.CharField(max_length=50, blank=False)
    customer_address_line_2 = models.CharField(max_length=50, blank=False)
    customer_pincode = models.CharField(max_length=10, blank=False)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    product_name = models.CharField(max_length=100, blank=False)
    product_serial_number = models.CharField(max_length=50, blank=True, null=True)
    product_amount = models.IntegerField(blank=False)
    finance_company = models.ForeignKey(FinanceCompany, on_delete=models.RESTRICT)
    finance_emi = models.IntegerField(default=0, blank=False)
    finance_dp = models.IntegerField(default=0,blank=False)
    finance_months = models.IntegerField(default=0,blank=False)
    finance_disbursement = models.IntegerField(default=0, blank=False)
    payment_cash = models.IntegerField(default=0, blank=False)
    payment_upi = models.IntegerField(default=0, blank=False)
    payment_debit_card = models.IntegerField(default=0, blank=False)
    payment_credit_card = models.IntegerField(default=0, blank=False)
    payment_net_banking = models.IntegerField(blank=False)
    exchange_value = models.IntegerField(default=0, blank=False)
    is_cancelled = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.series.name + "_" + self.invoice_no
    
    @property
    def is_financed(self):
        if self.finance_company.name != "No Finance":
            return True
        else: return False
        
    @property
    def expected_finance_disbursement(self):
        if self.is_financed == True:
            return self.product_amount - self.finance_dp
        else: return 0
        
    @property
    def is_finance_disbursement_pending(self):
        if self.is_financed == True and self.finance_disbursement == 0:
            return True
        else: return False
        
    @property
    def finance_disbursement_parity(self):
        return self.finance_disbursement - self.expected_finance_disbursement
    
    @property
    def amount_paid(self):
        paid = self.payment_cash + self.payment_upi + self.payment_credit_card + self.payment_debit_card + self.exchange_value
        if self.is_financed == True:
            paid = paid + self.expected_finance_disbursement
        return paid
    
    @property
    def amount_due(self):
        return self.product_amount - self.amount_paid
        
    @property
    def taxable_value(self):
        return round((self.product_amount / (100 + self.product_category.tax_rate)) * 100, 2)
    
    @property
    def cgst(self):
        return round((self.taxable_value * (self.product_category.tax_rate / 2)) / 100, 2)
    
    @property
    def sgst(self):
        return self.cgst
    
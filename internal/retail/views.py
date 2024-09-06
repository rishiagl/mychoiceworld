from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from retail.models import Merchant, ProductCategory, FinanceCompany, SingleProductInvoice, SingleProductInvoiceSeries
from django.template.loader import render_to_string
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from django.template.loader import render_to_string
import base64
from datetime import date, timedelta


def isPhoneNumberValid(customer_phone_number):
    if len(customer_phone_number) != 10:
        return False

    for letter in customer_phone_number:
        if letter < '0' or letter > '9':
            return False

    return True


@login_required(login_url="/admin/login/?next=/retail")
def index(request):
    today = date.today()
    d5_ago = today - timedelta(days=5)
    d7_ago = today - timedelta(days=7)
    d10_ago = today - timedelta(days=10)
    d15_ago = today - timedelta(days=15)
    d20_ago = today - timedelta(days=20)
    d25_ago = today - timedelta(days=25)
    d30_ago = today - timedelta(days=30)
    d60_ago = today - timedelta(days=60)
    d999_ago = today - timedelta(days=999)
    SingleProductInvoice_count = [SingleProductInvoice.objects.filter(invoice_date__range=(d5_ago, today), is_cancelled=False).count(), SingleProductInvoice.objects.filter(invoice_date__range=(d10_ago, d5_ago), is_cancelled=False).count(), SingleProductInvoice.objects.filter(invoice_date__range=(d15_ago, d10_ago), is_cancelled=False).count(
    ), SingleProductInvoice.objects.filter(invoice_date__range=(d20_ago, d15_ago), is_cancelled=False).count(), SingleProductInvoice.objects.filter(invoice_date__range=(d25_ago, d20_ago), is_cancelled=False).count(), SingleProductInvoice.objects.filter(invoice_date__range=(d30_ago, d25_ago), is_cancelled=False).count()][::-1]
    
    payment_breakup = [0,0,0,0,0,0]
    for singleProductInvoice in SingleProductInvoice.objects.filter(is_cancelled=False):
        payment_breakup[0] += singleProductInvoice.payment_cash
        payment_breakup[1] += singleProductInvoice.payment_upi
        payment_breakup[2] += singleProductInvoice.payment_debit_card
        payment_breakup[3] += singleProductInvoice.payment_credit_card
        payment_breakup[4] += singleProductInvoice.payment_net_banking
        payment_breakup[5] += singleProductInvoice.exchange_value

    customer_dues = 0
    for singleProductInvoice in SingleProductInvoice.objects.filter(is_cancelled=False):
        customer_dues += singleProductInvoice.amount_due
    
    disbursement_pending = 0
    for singleProductInvoice in SingleProductInvoice.objects.filter(is_cancelled=False):
        if(singleProductInvoice.is_finance_disbursement_pending == True):
            disbursement_pending += singleProductInvoice.expected_finance_disbursement
            
    total_sales = SingleProductInvoice.objects.filter(is_cancelled=False).count()
    this_week_sales = SingleProductInvoice.objects.filter(invoice_date__range=(d7_ago, today), is_cancelled=False).count()
    todays_sales = SingleProductInvoice.objects.filter(invoice_date=today, is_cancelled=False).count()

    return render(request, "retail/index.html", {"SingleProductInvoice_count": SingleProductInvoice_count, "total_sales": total_sales, "this_week_sales": this_week_sales, "todays_sales": todays_sales, "customer_dues": customer_dues, "disbursement_pending":disbursement_pending, "payment_breakup": payment_breakup})


@login_required(login_url="/admin/login/?next=/retail")
def sales_invoice(request):
    success_message = None
    error_message = None
    warning_message = None
    normal_message = None
    invoice_download_link = None
    print(request.POST)
    if request.method == "POST":
        series = SingleProductInvoiceSeries.objects.get(name="Default")
        merchant = Merchant.objects.get(name=request.POST['merchant'])
        name, code = request.POST['product_category'].split("_")
        product_category = ProductCategory.objects.get(name=name)
        finance_company = FinanceCompany.objects.get(
            name=request.POST['finance_company'])
        invoice_no = series.invoice_prefix + str(series.invoice_end_no + 1)
        invoice = SingleProductInvoice(series=series, invoice_date=request.POST['invoice_date'], invoice_no=invoice_no, merchant=merchant, customer_phone_number=request.POST['customer_phone_number'], customer_name=request.POST['customer_name'], customer_address_line_1=request.POST['address_line_1'], customer_address_line_2=request.POST['address_line_2'], customer_pincode=request.POST['address_pincode'], product_category=product_category, product_name=request.POST['product_name'], product_serial_number=request.POST['product_serial_no'], product_amount=int(
            request.POST['product_amount']), finance_company=finance_company, finance_emi=int(request.POST['finance_emi']), finance_dp=int(request.POST['finance_down_payment']), finance_months=int(request.POST['finance_months']), finance_disbursement=0, payment_cash=int(request.POST['cash_payment']), payment_upi=int(request.POST['upi_payment']), payment_debit_card=int(request.POST['debit_card_payment']), payment_credit_card=int(request.POST['credit_card_payment']), payment_net_banking=int(request.POST['net_banking_payment']), exchange_value=int(request.POST['exchange_value']))
        try:
            invoice.save()
            series.invoice_end_no = series.invoice_end_no + 1
            series.save()
            success_message = "Invoice Added Successfully"
            invoice_download_link = "/retail/sales_invoice/download/" + \
                str(invoice.invoice_no)
        except IntegrityError as e:
            warning_message = e
        except:
            error_message = "Please Contact Administrator Unwanted Error Occured"
        print(request.POST)
    merchants = Merchant.objects.all()
    product_categories = ProductCategory.objects.all()
    finance_companies = FinanceCompany.objects.all()
    print(product_categories)
    return render(request, "retail/sales_invoice.html", {"merchants": merchants, "product_categories": product_categories, "finance_companies": finance_companies, "success_message": success_message, "warning_message": warning_message, "error_message": error_message, "invoice_download_link": invoice_download_link})


login_required(login_url="/admin/login/?next=/retail")


def sales_invoice_by_invoice_no(request, invoice_no):
    invoice = SingleProductInvoice.objects.get(invoice_no=invoice_no)
    return render(request, "retail/sales_invoice_pdf.html", {"invoice": invoice})


def sales_invoice_download(request, invoice_no):

    invoice = SingleProductInvoice.objects.filter(invoice_no=invoice_no).first()
    if invoice != None:
        html_string = render_to_string(
            "retail/sales_invoice_pdf.html", {"invoice": invoice})
        invoice = invoice
        print(invoice)
    else:
        html_string = "<p>No Invoice Present</p>"

    # Write the HTML string to a temporary file
    temp_html_file = '/tmp/temp_pdf.html'
    with open(temp_html_file, 'w') as f:
        f.write(html_string)

    # Set up headless Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    # Specify the path to your ChromeDriver
    # chrome_driver_path = os.path.join(os.getcwd(), 'chromedriver')  # Adjust this path if necessary

    # Use the Service class to specify the ChromeDriver path
    service = Service(executable_path='/usr/bin/chromedriver')

    # Create a WebDriver instance with the service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Load the temporary HTML file in the browser
    driver.get(f'file://{temp_html_file}')

    # Generate the PDF
    pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {
        "format": "A4",           # Ensures A4 page size
        "marginTop": 0,           # No top margin
        "marginBottom": 0,        # No bottom margin
        "marginLeft": 0,          # No left margin
        "marginRight": 0,
        "scale": 1,
        "pageRanges": "1",  # No right margin
    })['data']

    # Decode the base64 PDF data
    pdf_data = base64.b64decode(pdf_data)

    driver.quit()

    # Serve the PDF as an HTTP response
    response = HttpResponse(pdf_data, content_type='application/pdf')
    filename = invoice_no
    response['Content-Disposition'] = 'inline; filename=' + filename + ".pdf"
    return response

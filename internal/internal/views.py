from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from register.models import Brand, Category, Product
from transactions.models import PurchaseInvoiceItem, PurchaseInvoice
from flipkart.models import Order
from django.utils.timezone import now
from retail.models import SingleProductInvoice
import datetime


@login_required(login_url="/admin/login/?next=/")
def index(request):
    return render(request, "index.html", {})


@login_required(login_url="/admin/login/?next=/")
def inventory(request):
    products = Product.objects.all().order_by('brand__name', 'category__name', 'model')
    return render(request, "inventory.html", {"products": products})


@login_required(login_url="/admin/login/?next=/")
def stock_history(request, id):
    list = PurchaseInvoiceItem.objects.filter(product__id=id)
    product = Product.objects.get(id=id)
    t_qty = 0
    t_amt = 0
    for l in list:
        t_qty = t_qty + l.qty
        t_amt = t_amt + l.total_amount
    avg_rate = 0
    if t_qty != 0:
        avg_rate = round(t_amt / t_qty)
    product_detail = {'name': product.name,
                      'total_qty': t_qty, 'average_rate': avg_rate}
    return render(request, "stock_history.html", {'product_detail': product_detail, 'list': list})


@login_required(login_url="/admin/login/?next=/")
def analysis(request):
    return HttpResponse("<h1>Under Construction</h1><a href='/'>Go Back</a>")


@login_required(login_url="/admin/login/?next=/")
def daybook(request):
    date = now()
    if request.method == "POST":
        date = request.POST['date']
    flipkart_orders = Order.objects.filter(order_date=date)
    sales_invoices = SingleProductInvoice.objects.filter(invoice_date=date)
    purchaseInvoices = PurchaseInvoice.objects.filter(invoice_date=date)
    return render(request, "daybook.html", {'flipkart_orders': flipkart_orders, 'sales_invoices': sales_invoices, 'purchaseInvoices': purchaseInvoices})

@login_required(login_url="/admin/login/?next=/")
def get_sales_invoice_html_by_inv_no(request, invoice_no):
    invoice = SingleProductInvoice.objects.filter(invoice_no=invoice_no).first()
    if invoice != None:
        invoice = invoice
        print(invoice)
    else:
        return HttpResponse("<h1>No Invoice with given Invoice No</h1><a href='/'>Go Back</a>")
    return render(request, "sales_invoice.html", {'invoice': invoice})

@login_required(login_url="/admin/login/?next=/")
def get_flipkart_order_html_order_id(request, order_id):
        return HttpResponse("<h1>Not Implemented till now Pls use this</h1><a href='/flipkart/'>Link</a>")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flipkart.models import Order
from django.db.utils import IntegrityError
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
from datetime import date, timedelta


@login_required(login_url="/admin/login/?next=/flipkart")
def index(request):
    today = date.today()
    d5_ago = today - timedelta(days=5)
    d10_ago = today - timedelta(days=10)
    d15_ago = today - timedelta(days=15)
    d20_ago = today - timedelta(days=20)
    d25_ago = today - timedelta(days=25)
    d30_ago = today - timedelta(days=30)
    order_count = [Order.objects.filter(order_date__range=(d5_ago, today)).count(), Order.objects.filter(order_date__range=(d10_ago, d5_ago)).count(), Order.objects.filter(order_date__range=(d15_ago, d10_ago)).count(), Order.objects.filter(order_date__range=(d20_ago, d15_ago)).count(), Order.objects.filter(order_date__range=(d25_ago, d20_ago)).count(), Order.objects.filter(order_date__range=(d30_ago, d25_ago)).count()][::-1]
    return render(request, "flipkart/index.html", {"order_count": order_count})


@login_required(login_url="/admin/login/?next=/flipkart/dispatch")
def dispatch(request):
    success_message = None
    error_message = None
    warning_message = None
    normal_message = None
    print(request.POST)
    if request.method == "POST":
        if not request.POST['file']:
            if not request.POST['order_id'] or not request.POST['tracking_id']:
                error_message = "Please enter both Order id and Tracking id"
            else:
                order_id = request.POST['order_id']
                tracking_id = request.POST['tracking_id']
                order_date = request.POST['order_date']
                order = Order(order_id=order_id,
                              tracking_id=tracking_id, order_date=order_date)
                try:
                    order.save()
                    success_message = "Order Added Successfully"
                except IntegrityError as e:
                    warning_message = e
                except:
                    error_message = "Please Contact Administrator Unwanted Error Occured"

        else:
            normal_message = "File Upload functionality not implemented"

    context = {"success_message": success_message, "error_message": error_message,
               "warning_message": warning_message, "normal_message": normal_message}

    return render(request, "flipkart/dispatch.html", context)


@login_required(login_url="/admin/login/?next=/flipkart/returns")
def returns(request):
    success_message = None
    error_message = None
    warning_message = None
    normal_message = None
    print(request.POST)
    if request.method == "POST":
        try:
            order = Order.objects.get(order_id=request.POST['order_id'])
            order.shipment_type = request.POST['shipment_type']
            order.delivery_status = 'RETURNED'
            order.delivery_date = now()
            print(now)
            order.save()
            success_message = "Order Marked Returned Successfully"
        except ObjectDoesNotExist:
            error_message = "Order Does Not Exist!"
        except Exception:
            error_message = "Some Internal Error Occured!"

    context = {"success_message": success_message, "error_message": error_message,
               "warning_message": warning_message, "normal_message": normal_message}

    return render(request, "flipkart/returns.html", context)


@login_required(login_url="/admin/login/?next=/flipkart/payments")
def payments(request):
    success_message = None
    error_message = None
    warning_message = None
    normal_message = None
    print(request.POST)
    if request.method == "POST":
        try:
            order = Order.objects.get(order_id=request.POST['order_id'])
            order.final_settlement = order_id = request.POST['final_settlement']
            order.save()
            success_message = "Payment Recieved Successfully"
        except ObjectDoesNotExist:
            error_message = "Order Does Not Exist!"
        except Exception:
            error_message = "Some Internal Error Occured!"

    context = {"success_message": success_message, "error_message": error_message,
               "warning_message": warning_message, "normal_message": normal_message}

    return render(request, "flipkart/payments.html", context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flipkart.models import Order
from django.db.utils import IntegrityError
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url="/admin/login/?next=/flipkart")
def index(request):
    return render(request, "flipkart/index.html", {})


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
                if len(request.POST['order_id']) != 20:
                    error_message = "Order String Validation failed"
                else:
                    order_id = request.POST['order_id']
                    tracking_id = request.POST['tracking_id']
                    order = Order(order_id=order_id, tracking_id=tracking_id)
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

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sales_invoice", views.sales_invoice, name="sales_invoice"),
    path("sales_invoice/<str:invoice_no>", views.sales_invoice_by_invoice_no, name="sales_invoice"),
    path("sales_invoice/download/<str:invoice_no>", views.sales_invoice_download, name="sales_invoice"),
]
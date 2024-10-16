"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('inventory', views.inventory, name="inventory"),
    path('inventory/<int:id>/', views.stock_history, name="stock_history"),
    path('analysis', views.analysis, name="analysis"),
    path('daybook', views.daybook, name="daybook"),
    path('sales_invoice/<str:invoice_no>/', views.get_sales_invoice_html_by_inv_no, name="get_sales_invoice_html_by_inv_no"),
    path('flipkart/<str:order_id>/', views.get_flipkart_order_html_order_id, name="get_flipkart_order_html_order_id"),
    path("__reload__/", include("django_browser_reload.urls")),
    path('flipkart/', include("flipkart.urls")),
    path('retail/', include("retail.urls")),
    path('register/', include("register.urls")),
    path('transactions/', include("transactions.urls")),
    path('admin/', admin.site.urls),
]

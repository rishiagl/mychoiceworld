from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('callbackrequest/', views.CallbackRequests_list),
]
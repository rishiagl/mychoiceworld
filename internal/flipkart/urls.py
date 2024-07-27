from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dispatch", views.dispatch, name="dispatch"),
    path("returns", views.returns, name="returns"),
]
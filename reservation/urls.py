from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("table/", views.table_details, name="table"),
    path("customer/", views.customer_details, name="customer")
]

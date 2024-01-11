from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReservationListView.as_view(), name="reservation-list"),
    path("<int:id>", views.ReservationDetailView.as_view(), name="reservation-details"),
    path("create", views.ReservationCreateWizardView.as_view(), name="reservation-create"),
]

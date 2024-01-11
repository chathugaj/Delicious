from django.urls import path

from . import views

app_name = 'reservation'
urlpatterns = [
    path("", views.ReservationListView.as_view(), name="reservation-list"),
    path("create/", views.ReservationCreateWizardView.as_view(), name="reservation-create"),
    path("<int:id>/", views.ReservationDetailView.as_view(), name="reservation-details"),
    path("<int:id>/update/", views.ReservationUpdateView.as_view(), name="reservation-update"),
    path("<int:id>/delete/", views.ReservationDeleteView.as_view(), name="reservation-delete")
]

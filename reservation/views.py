from datetime import date, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from formtools.wizard.views import SessionWizardView

from The_Dine_restaurant.settings import EMAIL_HOST_USER
from .forms import ReservationModelForm, CustomerModelForm
from .models import Reservation, Customer


# Create your views here.

class ReservationListView(LoginRequiredMixin, ListView):
    template_name = 'reservation/reservation_list.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            # return all bookings until before yesterday
            return Reservation.objects.filter(reservation_date__gt=(date.today() - timedelta(days=1)))
        else:
            return Reservation.objects.filter(username=self.request.user.username, reservation_date__gt=(date.today() - timedelta(days=1)))


class ReservationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'reservation/reservation_detail.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reservation, id=id_)


class ReservationConfirmationView(DetailView):
    template_name = 'reservation/reservation_confirmation.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reservation, id=id_)


class ReservationUpdateView(UpdateView):
    """Render the reservation form"""
    form_class = ReservationModelForm
    template_name = 'reservation/reservation_update.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reservation, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class ReservationDeleteView(DeleteView):
    """Render the reservation form"""
    template_name = 'reservation/reservation_delete.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reservation, id=id_)

    def get_success_url(self):
        return reverse('reservation:reservation_list')


class ReservationCreateWizardView(LoginRequiredMixin, SessionWizardView):
    """This view handles the multi-step table reservation"""
    form_list = [ReservationModelForm, CustomerModelForm]
    template_name = 'reservation/reservation_create.html'

    def done(self, form_list, form_dict, **kwargs):
        reservation_form = form_dict['0']
        customer_form = form_dict['1']

        customer = customer_form.save(commit=False)
        customer_email = customer
        customer.username = self.request.user.username
        customer.save()

        customer_ = list(Customer.objects.all().filter(email=customer_email))[0]

        # Save without committing to the database
        reservation = reservation_form.save(commit=False)
        reservation.customer = customer_
        reservation.username = self.request.user.username
        assignable_table_response = ReservationModelForm.find_assignable_table(reservation.reservation_date, reservation.time_slot,
                                                                               reservation.number_of_guests)
        if assignable_table_response is None:
            raise RuntimeError("Unfortunately we couldn't find any available tables for the day. Please contact us through the phone.")
        reservation.table = assignable_table_response

        # Commit to the database
        reservation.save()

        content = render_to_string("reservation/email/reservation_confirmation.txt", {
            "first_name": customer_.first_name,
            "last_name":customer_.last_name,
            "reservation_date": reservation.reservation_date,
            "time_slot": reservation.time_slot,
            "number_of_guests": reservation.number_of_guests,
        })
        send_mail("The Dine Restaurant: Table reservation confirmed", content, EMAIL_HOST_USER, [customer_email], fail_silently=True)

        return HttpResponseRedirect("/reservation/confirmation/{}".format(reservation_form.instance.id))

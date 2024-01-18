from datetime import date, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from formtools.wizard.views import SessionWizardView

from .forms import ReservationModelForm, CustomerModelForm
from .models import Reservation, Customer, Table

from django.core.mail import send_mail
from The_Dine_restaurant.settings import EMAIL_HOST_USER


# Create your views here.

class ReservationListView(LoginRequiredMixin, ListView):
    template_name = 'reservation/reservation_list.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            # return all bookings until before yesterday
            return Reservation.objects.filter(reservation_date__gt=(date.today() - timedelta(days=1)))
        else:
            customer_ = list(Customer.objects.filter(email=self.request.user.username))[0]
            return Reservation.objects.filter(customer=customer_, reservation_date__gt=(date.today() - timedelta(days=1)))


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
        print(form.cleaned_data)
        return super().form_valid(form)


class ReservationDeleteView(DeleteView):
    """Render the reservation form"""
    template_name = 'reservation/reservation_delete.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reservation, id=id_)

    def get_success_url(self):
        return reverse('reservation:reservation-list')


class ReservationCreateWizardView(SessionWizardView):
    """This view handles the multi-step table reservation"""
    form_list = [ReservationModelForm, CustomerModelForm]
    template_name = 'reservation/reservation_create.html'

    def done(self, form_list, form_dict, **kwargs):
        reservation_form = form_dict['0']
        customer_form = form_dict['1']

        customer_email = customer_form.instance
        customer_ = list(Customer.objects.all().filter(email=customer_email))[0]
        if customer_ is None:
            customer_email = customer_form.save()
            customer_ = list(Customer.objects.all().filter(email=customer_email))[0]

        # Save without committing to the database
        reservation = reservation_form.save(commit=False)
        reservation.customer = customer_
        assignable_table_response = ReservationModelForm.find_assignable_table(reservation.reservation_date, reservation.time_slot,
                                                                               reservation.number_of_guests)
        if (assignable_table_response is None):
            raise RuntimeError("Unfortunately we couldn't find any available tables for the day. Please contact us through the phone.")
        reservation.table = assignable_table_response

        # Commit to the database
        reservation.save()

        send_mail("The Dine Restaurant: Table reservation confirmed", "Test", EMAIL_HOST_USER, [customer_email], fail_silently=True)

        return HttpResponseRedirect("/reservation/confirmation/{}".format(reservation_form.instance.id))
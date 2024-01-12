from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from formtools.wizard.views import SessionWizardView

from .forms import ReservationModelForm, CustomerModelForm
from .models import Reservation, Customer, Table


# Create your views here.

class ReservationListView(ListView):
    template_name = 'reservation/reservation_list.html'
    queryset = Reservation.objects.all()


class ReservationDetailView(DetailView):
    template_name = 'reservation/reservation_detail.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reservation, id=id_)


# class ReservationCreateView(CreateView):
#     """Render the reservation form"""
#     form_class = ReservationModelForm
#     template_name = 'reservation/reservation_update.html'
#     queryset = Reservation.objects.all()
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
#
#     def get_object(self, queryset=None):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Reservation, id=id_)


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
        customer_email = form_dict['1'].save()
        customer_ = list(Customer.objects.all().filter(email=customer_email))[0]

        # Save without committing to the database
        reservation_form = form_dict['0']
        reservation = reservation_form.save(commit=False)
        reservation.customer = customer_

        # Commit to the database
        reservation.save()

        return HttpResponseRedirect("/reservation/{}".format(reservation_form.instance.id))
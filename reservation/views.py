from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from formtools.wizard.views import SessionWizardView

from .forms import ReservationModelForm, CustomerModelForm
from .models import Reservation


# Create your views here.

class ReservationListView(ListView):
    template_name = 'reservation/reservation_list.html'
    queryset = Reservation.objects.all()


class ReservationDetailView(DetailView):
    template_name = 'reservation/reservation_detail.html'
    queryset = Reservation.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reservation, id=id_)


class ReservationCreateView(CreateView):
    """Render the reservation form"""
    form_class = ReservationModelForm
    template_name = 'reservation/reservation_create.html'
    queryset = Reservation.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Reservation, id=id_)


class ReservationCreateWizardView(SessionWizardView):
    """This view handles the multi-step table reservation"""
    form_list = [ReservationModelForm, CustomerModelForm]

    def done(self, form_list, form_dict, **kwargs):
        customer = form_dict['customer'].save()
        reservation = form_dict['reservation'].save()
        return HttpResponseRedirect('reservation/reservation-detail.html')


def customer_details(request):
    context = {
        "reservation_date": request.POST['reservation_date'],
        "time_slot": request.POST['time_slot'],
        "number_of_guests": request.POST['number_of_guests']
    }

    return render(request, "reservation/customer_details_form.html", context)
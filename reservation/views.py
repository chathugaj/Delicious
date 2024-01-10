from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView

from .forms import ReservationModelForm
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


def customer_details(request):
    context = {
        "reservation_date": request.POST['reservation_date'],
        "time_slot": request.POST['time_slot'],
        "number_of_guests": request.POST['number_of_guests']
    }

    return render(request, "reservation/customer_details_form.html", context)
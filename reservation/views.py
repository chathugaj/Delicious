from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import dateparse
from django.views.generic import CreateView, ListView, DetailView

from .models import Customer, Reservation
from .forms import ReservationModelForm

# Create your views here.

# def confirmation(request):
#     reservation_date = request.POST['reservation_date']
#     time_slot = request.POST['time_slot']
#     number_of_guests = request.POST['number_of_guests']
#     first_name = request.POST['first_name']
#     last_name = request.POST['last_name']
#     email = request.POST['email']
#     phone = request.POST['phone']
#
#     Customer(first_name=first_name, last_name=last_name, email=email, phone=phone).save()
#     c = Customer.objects.last()
#
#     res = Reservation.objects.last()
#
#     context = {
#         "reservation_date": res.reservation_date,
#         # "time_slot": t.time_slot,
#         "number_of_guests": res.number_of_guests,
#         "name": '{} {}'.format(c.first_name, c.last_name),
#         "email": c.email,
#         "phone": c.phone
#     }
#     return render(request, "reservation/confirmation.html", context)


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
    success_url = '/reservation/reservation_customer_create.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
        # reservation_date = form.cleaned_data['reservation_date']
        # time_slot = form.cleaned_data['time_slot']
        # number_of_guests = form.cleand_data['number_of_guests']
        #
        # messages.success(
        #     self.request,
        #     f'Reservation confirmed for {number_of_guests} guests on {reservation_date} for {time_slot}'
        # )
        #
        # return super(ReservationCreateView, self).form_valid(form)

# def table_details(request):
#     reservation_form = ReservationForm()
#
#     return render(request, "reservation/table_reservation.html", {"reservation_form": reservation_form})
#
#
def customer_details(request):
    context = {
        "reservation_date": request.POST['reservation_date'],
        "time_slot": request.POST['time_slot'],
        "number_of_guests": request.POST['number_of_guests']
    }

    return render(request, "reservation/customer_details_form.html", context)
#
#
# def reservations(request):
#     reservations = Reservation.objects.all()
#     context = {
#         "reservation_details": reservations
#     }
#     return render(request, "reservation/reservations.html", context)
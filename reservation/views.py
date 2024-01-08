from django.shortcuts import render
from django.http import HttpResponse
from django.utils import dateparse

from .models import Customer, Reservation
from .forms import ReservationForm

# Create your views here.

def confirmation(request):
    reservation_date = request.POST['reservation_date']
    time_slot = request.POST['time_slot']
    number_of_guests = request.POST['number_of_guests']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']

    Customer(first_name=first_name, last_name=last_name, email=email, phone=phone).save()
    c = Customer.objects.last()

    res = Reservation.objects.last()

    context = {
        "reservation_date": res.reservation_date,
        # "time_slot": t.time_slot,
        "number_of_guests": res.number_of_guests,
        "name": '{} {}'.format(c.first_name, c.last_name),
        "email": c.email,
        "phone": c.phone
    }
    return render(request, "reservation/confirmation.html", context)


def table_details(request):
    reservation_form = ReservationForm()

    return render(request, "reservation/table_details.html", {"reservation_form": reservation_form})


def customer_details(request):
    context = {
        "reservation_date": request.POST['reservation_date'],
        "time_slot": request.POST['time_slot'],
        "number_of_guests": request.POST['number_of_guests']
    }

    return render(request, "reservation/customer_details.html", context)


def reservations(request):
    reservations = Reservation.objects.all()
    context = {
        "reservation_details": reservations
    }
    return render(request, "reservation/reservations.html", context)
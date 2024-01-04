from django.shortcuts import render
from django.http import HttpResponse

from .models import TimeSlot

# Create your views here.


def index(request):
    return HttpResponse("RESERVATION index")


def reservations(request):
    return HttpResponse("reservations")


def table_details(request):
    time_slot_list = TimeSlot.objects.all()
    context = {
        "time_slot_list": time_slot_list
    }
    return render(request, "reservation/table_details.html", context)


def customer_details(request):
    context = {
        "reservation_date": request.POST['reservation_date'],
        "time_slot": request.POST['time_slot'],
        "number_of_guests": request.POST['number_of_guests']
    }

    return render(request, "reservation/customer_details.html", context)

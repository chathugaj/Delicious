from datetime import date
from django import forms

from .models import Reservation, Customer, TIME_SLOTS

TIME_SLOT_CHOICE = dict((str(k), v) for k, v in TIME_SLOTS)


class ReservationForm(forms.ModelForm):

    """Form to create reservations"""
    class Meta:
        """Fields for the form"""
        model = Reservation
        fields = [
            'reservation_date', 'time_slot', 'number_of_guests'
        ]
        reservation_date = forms.DateField()


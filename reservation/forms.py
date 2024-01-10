from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Reservation


class ReservationForm(forms.ModelForm):
    """Form to create reservations"""

    class Meta:
        """Fields for the form"""
        model = Reservation
        fields = ['reservation_date', 'time_slot', 'number_of_guests']

        widgets = {
            'reservation_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }
        labels = {
            'reservation_date': 'Date',
            'time_slot': 'Time',
            'number_of_guests': 'Number Of Guests',
        }

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data['reservation_date']

        if reservation_date < timezone.now().date():
            raise ValidationError('Reservation date must be in the future.')

        return reservation_date

    def clean_number_of_guests(self):
        number_of_guests = self.cleaned_data['number_of_guests']

        if number_of_guests <= 0:
            raise ValidationError('Number of guests must be a positive integer.')

        return number_of_guests



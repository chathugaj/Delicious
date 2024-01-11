from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Reservation, Customer


class ReservationModelForm(forms.ModelForm):
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


class CustomerModelForm(forms.ModelForm):
    """Form to create customer record"""

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
        }
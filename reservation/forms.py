from django import forms
from django.db.models import Count
from django.utils import timezone

from .models import Reservation, Customer, TABLE_CAPACITIES, Table


class ReservationModelForm(forms.ModelForm):
    """Form to create reservations"""

    class Meta:
        """Fields for the form"""
        model = Reservation
        fields = ['reservation_date', 'time_slot', 'number_of_guests']
        exclude = ('customer', 'table')

        max_guests = max([t[0] for t in list(TABLE_CAPACITIES)])

        widgets = {
            'reservation_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date',
                       'min': timezone.now,
                       }),
        }
        labels = {
            'reservation_date': 'Date',
            'time_slot': 'Time',
            'number_of_guests': 'Number Of Guests',
        }

    @staticmethod
    def send_email():
        print("Inside send email")
        pass

    @staticmethod
    def find_assignable_table(reservation_date, time_slot, number_of_guests):
        reservations_time_slot = Reservation.objects.all().filter(reservation_date=reservation_date, time_slot=time_slot)
        # reservations_counts_per_table = (Reservation.objects.all().filter(reservation_date=reservation_date)
        #                          .values('table', 'time_slot').annotate(total=Count('table')).order_by('total'))
        #
        # print(">>>>reservations_counts_per_table", reservations_counts_per_table)

        assignable_capacities = [t[0] for t in list(TABLE_CAPACITIES) if t[0] >= number_of_guests]
        assignable_tables = Table.objects.filter(capacity__in=assignable_capacities).order_by("capacity")

        booked_table_counts = {x.id: 0 for x in assignable_tables}

        for rt in reservations_time_slot:
            if rt.table.id in booked_table_counts:
                booked_table_counts[rt.table.id] = booked_table_counts[rt.table.id] + 1
            else:
                booked_table_counts[rt.table.id] = 1

        if len(booked_table_counts) > 0:
            table_available = [at for at in assignable_tables if
                               at.id in booked_table_counts and booked_table_counts[at.id] < at.number_of_tables]
            if len(table_available) == 0:
                return None
            return table_available[0]
        else:
            return list(assignable_tables)[0]

    def clean(self):
        # Get reserved tables for the same time date and time slot as this reservation
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get("reservation_date")
        time_slot = cleaned_data.get("time_slot")
        number_of_guests = cleaned_data['number_of_guests']

        max_guests = max([t[0] for t in list(TABLE_CAPACITIES)])

        if number_of_guests is None or number_of_guests == '':
            raise forms.ValidationError("Number of gusts is required")

        if number_of_guests > max_guests:
            raise forms.ValidationError("We can support only up to {} guests".format(max_guests))

        if number_of_guests < 1:
            raise forms.ValidationError("Invalid number of guests")

        if reservation_date is None or reservation_date == '':
            raise forms.ValidationError("This field is required")

        if reservation_date < timezone.now().date():
            raise forms.ValidationError("This field requires today or a future date")

        assignable_table_response = ReservationModelForm.find_assignable_table(reservation_date, time_slot, number_of_guests)
        if assignable_table_response is None:
            raise forms.ValidationError("We could not find any tables for the time slot")

        return cleaned_data


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

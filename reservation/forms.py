from django import forms
from django.utils import timezone

from .models import Reservation, Customer, TABLE_CAPACITIES, Table



class ReservationModelForm(forms.ModelForm):
    """Form to create reservations"""

    class Meta:
        """Fields for the form"""
        model = Reservation
        fields = ['reservation_date', 'time_slot', 'number_of_guests']
        exclude = ('customer', 'table_number')

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

    # def clean_number_of_guests(self):
    #     cleaned_data = super().clean()
    #     number_of_guests = cleaned_data.get('number_of_guests')
    #
    #     max_guests = max([t[0] for t in list(TABLE_CAPACITIES)])
    #
    #     if number_of_guests is None or number_of_guests == '':
    #         raise forms.ValidationError("Number of gusts is required")
    #
    #     if number_of_guests > max_guests:
    #         raise forms.ValidationError("We can support only up to {} guests".format(max_guests))
    #
    #     if number_of_guests < 1:
    #         raise forms.ValidationError("Invalid number of guests")
    #
    # def clean_reservation_date(self):
    #     """Validate reservation_date field"""
    #     cleaned_data = super().clean()
    #     reservation_date = cleaned_data.get('reservation_date')
    #     time_slot = cleaned_data.get('time_slot')
    #     number_of_guests = cleaned_data.get('number_of_guests')
    #     print(">>> time_slot", time_slot, reservation_date, number_of_guests)
    #
    #     if reservation_date is None or reservation_date == '':
    #         raise forms.ValidationError("This field is required")
    #
    #     if reservation_date < timezone.now().date():
    #         raise forms.ValidationError("This field requires today or a future date")

    @staticmethod
    def find_assignable_table(reservation_date, time_slot, number_of_guests):
        print(">>> time_slot", time_slot)
        print(">>> reservation_date", reservation_date)
        reservations = Reservation.objects.all().filter(reservation_date=reservation_date, time_slot=time_slot)
        print(">>>> reservations", reservations)

        print(">>>>number_of_guests", number_of_guests)
        assignable_capacities = [t[0] for t in list(TABLE_CAPACITIES) if t[0] >= number_of_guests]
        print(">>>>assignable_capacities", assignable_capacities)
        assignable_tables = Table.objects.filter(capacity__in=assignable_capacities).order_by("capacity")
        print(">>>>assignable_tables", assignable_tables)

        booked_table_counts = {x.id: 0 for x in assignable_tables}

        for rt in reservations:
            if rt.table_number in booked_table_counts:
                booked_table_counts[rt.table_number] = booked_table_counts[rt.table_number] + 1
            else:
                booked_table_counts[rt.table_number] = 1

        print(assignable_capacities)
        print(">>>>assignable_capacities", assignable_capacities)
        print(booked_table_counts)
        print(">>>>booked_table_counts", booked_table_counts)

        if len(booked_table_counts) > 0:
            table_available = [at for at in assignable_tables if
                               at.id in booked_table_counts and booked_table_counts[at.id] < at.capacity]
            print(">>>>> table_available", table_available)
            if len(table_available) == 0:
                return None
                # raise forms.ValidationError("We could not find any tables for the time slot")
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

        assignable_table = ReservationModelForm.find_assignable_table(reservation_date, time_slot, number_of_guests)
        if assignable_table is None:
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

    # def save(self, commit=True):
    #     """Get the temp customer object"""
    #     temp_customer = Customer.objects.all().filter(email='temp@thedine').first()
    #     print(temp_customer)
    #     temp_reservation = Reservation.objects.all().filter(customer__email=temp_customer.email).first()
    #
    #
    #     customer_ = super().save(commit)
    #     temp_reservation.customer = customer_
    #     temp_reservation.save(commit)

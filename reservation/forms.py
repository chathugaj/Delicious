from django import forms
from django.utils import timezone

from .models import Reservation, Customer, TABLE_CAPACITIES


class ReservationModelForm(forms.ModelForm):
    """Form to create reservations"""

    class Meta:
        """Fields for the form"""
        model = Reservation
        fields = ['reservation_date', 'time_slot', 'number_of_guests', 'table_number']
        exclude = ('customer',)

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

    def clean_number_of_guests(self):
        number_of_guests = self.cleaned_data.get('number_of_guests')
        max_guests = max([t[0] for t in list(TABLE_CAPACITIES)])

        if number_of_guests is None or number_of_guests == '':
            raise forms.ValidationError("Number of gusts is required")

        if number_of_guests > max_guests:
            raise forms.ValidationError("We can support only up to {} guests".format(max_guests))

        if number_of_guests < 1:
            raise forms.ValidationError("Invalid number of guests")

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data.get('reservation_date')

        if reservation_date is None or reservation_date == '':
            raise forms.ValidationError("This field is required")

        if reservation_date < timezone.now().date():
            raise forms.ValidationError("This field requires today or a future date")




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

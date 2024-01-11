from django import forms

from .models import Reservation, Customer


class ReservationModelForm(forms.ModelForm):
    """Form to create reservations"""

    class Meta:
        """Fields for the form"""
        model = Reservation
        fields = ['reservation_date', 'time_slot', 'number_of_guests', 'table_number']
        exclude = ('customer',)

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

    # def save(self, commit=True):
    #     """Assign a temporary customer to the reservqtion"""
    #     obj, created = Customer.objects.get_or_create(
    #         first_name='Internal',
    #         last_name='Pending',
    #         email='temp@thedine',
    #         temp=True
    #     )
    #
    #     self.cleaned_data['customer'] = obj.id
    #     return super().save(commit)


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
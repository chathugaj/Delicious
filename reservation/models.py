from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone

# Create your models here.

# Choices
TIME_SLOTS = (
    (1, "16:00 - 17:30"), (2, "17:30 - 19:00"), (3, "19:00 - 20:30"), (4, "20:30 - 22:00")
)
TABLE_CAPACITIES = (
    (2, "2"), (4, "4"), (6, "6"), (8, "8")
)


class Table(models.Model):
    """The model that handles restaurant table data"""
    number_of_tables = models.IntegerField(default=4)
    capacity = models.IntegerField(choices=TABLE_CAPACITIES, default=2)

    class Meta:
        """Order By table_number"""
        ordering = ['capacity']

    def __str__(self) -> str:
        return str('Capacity {}'.format(self.capacity))


class Customer(models.Model):
    """The model handles  the customer data"""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=23)
    username = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.email)


class Reservation(models.Model):
    """The model that handles the reservations"""
    time_slot = models.IntegerField(choices=TIME_SLOTS, default=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_date = models.DateField(default=timezone.now)
    number_of_guests = models.IntegerField(default=2)
    table = models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    username = models.CharField(max_length=100, null=True)


    class Meta:
        """Ordering with reservation_date and time_slot"""
        ordering = ['reservation_date', 'time_slot']

    def __str__(self) -> str:
        return str('{} {} {}'.format(self.customer, self.reservation_date, self.time_slot))

    def get_absolute_url(self):
        return reverse('reservation:reservation-details', kwargs={"id": self.id})

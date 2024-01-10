from django.db import models
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
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=TABLE_CAPACITIES, default=2)

    class Meta:
        """Order By table_number"""
        ordering = ['table_number']

    def __str__(self) -> str:
        return str(self.table_number)


class Customer(models.Model):
    """The model handles  the customer data"""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=18)

    def __str__(self) -> str:
        return str('{} {}'.format(self.first_name, self.last_name))


class Reservation(models.Model):
    """The model that handles the reservations"""
    time_slot = models.IntegerField(choices=TIME_SLOTS, default=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_date = models.DateField(default=timezone.now)
    number_of_guests = models.IntegerField(default=2)
    table_number = models.ForeignKey(Table, on_delete=models.DO_NOTHING)

    class Meta:
        """Ordering with reservation_date and time_slot"""
        ordering = ['reservation_date', 'time_slot']

    def __str__(self) -> str:
        return str(self.reservation_date)

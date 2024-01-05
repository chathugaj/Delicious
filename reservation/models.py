from django.db import models

# Create your models here.


class TimeSlot(models.Model):
    time_slot = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.time_slot


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=18)

    def __str__(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)


class Reservation(models.Model):
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_date = models.DateField("Reservation date")
    number_of_guests = models.IntegerField(default=2)

    def __str__(self) -> str:
        return self.reservation_date

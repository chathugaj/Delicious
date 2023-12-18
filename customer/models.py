from django.db import models

# Create your models here.


class Booking(models.Model):
    create_date_time = models.DateTimeField("create date_time")
    Booking_date_time = models.DateTimeField("booking date_time")
    guests = models.IntegerField(default=1)


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

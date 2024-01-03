from django.contrib import admin

from .models import TimeSlot, Customer, Reservation

# Register your models here.
admin.site.register(TimeSlot)
admin.site.register(Customer)
admin.site.register(Reservation)

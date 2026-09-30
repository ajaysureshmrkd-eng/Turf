from django.db import models

from booking.models import Truf

# Create your models here.


class BookingSlot(models.Model):

    customer_name =models.CharField(max_length=200)

    phone =models.CharField(max_length=15)

    turf=models.ForeignKey(Truf,on_delete=models.CASCADE)
    
    booking_date =models.DateField()

    booking_time =models.TimeField()

    duration =models.PositiveIntegerField()

    email=models.EmailField()


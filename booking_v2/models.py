from django.db import models


# Create your models here.
from booking.models import Truf

class booking(models.Model):


    team_name =models.CharField(max_length=200)

    turf =models.ForeignKey(Truf,on_delete=models.CASCADE)

    phone_number =models.CharField(max_length=15)

    email =models.EmailField()

    date =models.DateField()

    start_time =models.TimeField()

    end_time =models.TimeField()

    match_duration =models.DurationField()


    def __str__(self):
        return f"{self.team_name} - {self.turf}"


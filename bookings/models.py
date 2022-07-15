from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    Date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return self.name

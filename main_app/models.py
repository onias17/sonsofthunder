from django.db import models

# Create your models here.
class Appointment(models.Model):
    building = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

appointments = [
    Appointment('Residential', 'need ligthing fixtures installed in the bathroom', '123 Residential Way', '12/20/20'),
    Appointment('Commercial', 'need upgraded panels', '456 Commercial Rd', '12/21/20'),
    Appointment('Industrial', 'need electrical ground work to be completed', '789 Industrial Ave', '12/22/20'),
];
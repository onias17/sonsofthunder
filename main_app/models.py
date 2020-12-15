from django.db import models
from django.utils import timezone

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigAutoField
    email = models.EmailField(max_length=100)
    building_type = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)

appointments = [
    Appointment('Residential', 'need ligthing fixtures installed in the bathroom', '123 Residential Way', '12/20/20'),
    Appointment('Commercial', 'need upgraded panels', '456 Commercial Rd', '12/21/20'),
    Appointment('Industrial', 'need electrical ground work to be completed', '789 Industrial Ave', '12/22/20'),
];
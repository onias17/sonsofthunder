from django.db import models
from django.utils import timezone

# Create your models here.
BUILDING = (
    ('R', 'Residential'),
    ('C', 'Commercial'),
    ('I', 'Industrial'),
)

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigAutoField
    email = models.EmailField(max_length=100)
    building_type = models.CharField(
        max_length=1,
        choices=BUILDING,
    )
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)

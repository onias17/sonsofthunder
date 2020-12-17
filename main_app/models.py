from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
BUILDING = (
    ('R', 'Residential'),
    ('C', 'Commercial'),
    ('I', 'Industrial'),
)

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(
        'Phone Number', 
        max_length=13
    )
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    building_type = models.CharField(
        'Building Type',
        max_length=1,
        choices=BUILDING,
    )
    description = models.TextField(
        'Description of services needed',
        max_length=500,
    )
    date = models.DateTimeField(
        'Appointment Date', 
        auto_now=False, 
        auto_now_add=False,
    )
    date_created = models.DateTimeField(auto_now_add=True)



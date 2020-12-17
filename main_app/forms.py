from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'name', 
            'phone',
            'email', 
            'building_type', 
            'address', 
            'description', 
            'date'
        ]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment

# HOME and ABOUT
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# APPOINTMENTS
def appointments_index(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/index.html', { 'appointments': appointments })

def appointments_detail(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'appointments/detail.html', { 'appointment': appointment })
from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment

# HOME and ABOUT
def home(request):
    return HttpResponse('<h1>Sons of Thunder</h1>')

def about(request):
    return render(request, 'about.html')

# APPOINTMENTS
def appointments_index(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/index.html', { 'appointments': appointments })

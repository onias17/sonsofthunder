from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Appointment
from .forms import AppointmentForm

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

def add_appointment(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            new_appointment = appointment_form.save(commit=False)
            new_appointment.save()
            return redirect('detail', new_appointment.id)
        else: 
            form = AppointmentForm()
            context = { 'form': form }
            return render(request, 'appointments/new.html', context)

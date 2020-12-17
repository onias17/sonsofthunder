from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

# HOME and ABOUT
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# APPOINTMENTS
@login_required
def appointments_index(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointments_form.is_valid():
            new_appointment = appointment_form.save(commit=False)
            new_appointment.user = request.user
            new_appointment.save()
            return redirect('appointments_index')
    appointments = Appointment.objects.all()
    appointment_form = AppointmentForm()
    context = { 'appointments': appointments, 'appointment_form': appointment_form }
    return render(request, 'appointments/index.html', context)

@login_required
def appointments_detail(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'appointments/detail.html', { 'appointment': appointment })

def add_appointment(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            new_appointment = appointment_form.save(commit=False)
            new_appointment.save()
            return redirect('home')
    else: 
        form = AppointmentForm()
        context = { 'form': form }
        return render(request, 'appointments/new.html', context)

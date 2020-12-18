from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, mail_admins
from django.conf import settings

# HOME and ABOUT
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# APPOINTMENTS
@login_required
def appointments_index(request):
    appointments = Appointment.objects.all()
    context = { 'appointments': appointments }
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
            mail_admins(
                "New Inquiry",
                "test...",
                fail_silently=False,
                connection=None,
                html_message=None,
            )
            send_mail(
                "Inquiry",
                "Thank You! We have received your inquiry! " + new_appointment.address + "" + new_appointment.building_type + "" + new_appointment.description,
                "oniasnephiisrael@gmail.com",
                [new_appointment.email],
                fail_silently=False,
            )
            return redirect('home')
    else: 
        form = AppointmentForm()
        context = { 'form': form }
        return render(request, 'appointments/new.html', context)

@login_required
def delete_appointment(request, appointment_id):
    Appointment.objects.get(id=appointment_id).delete()
    return redirect('home')    
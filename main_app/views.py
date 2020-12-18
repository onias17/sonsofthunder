from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, mail_admins
from django.conf import settings
from django.template import loader

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
            message = loader.render_to_string(
                'emails/admin1.html',
                {
                    'name': new_appointment.name,
                    'phone_number': new_appointment.phone,
                    'email': new_appointment.email,
                    'address': new_appointment.address,
                    'building_type': new_appointment.building_type,
                    'description': new_appointment.description,
                    'date_created': new_appointment.date_created,
                }
            )
            mail_admins(
                "New Inquiry",
                "test...",
                fail_silently=False,
                connection=None,
                html_message=message,
            )
            html_message = loader.render_to_string(
                'emails/client1.html',
                {
                    'subject': 'Thank you, We have received your inquiry!',
                    'address': new_appointment.address,
                    'building_type': new_appointment.building_type,
                    'description': new_appointment.description,
                }
            )
            send_mail(
                "Inquiry",
                "Thank you, we have received your inquiry. ",
                "oniasnephiisrael@gmail.com",
                [new_appointment.email],
                fail_silently=False,
                html_message=html_message
            )
            return render(request, 'appointments/success.html')
    else: 
        form = AppointmentForm()
        context = { 'form': form }
        return render(request, 'appointments/new.html', context)

def edit_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST, instance=appointment)
        if appointment_form.is_valid():
            new_appointment = appointment_form.save()
            message = loader.render_to_string(
                'emails/admin2.html',
                {
                    'name': new_appointment.name,
                    'phone_number': new_appointment.phone,
                    'email': new_appointment.email,
                    'address': new_appointment.address,
                    'building_type': new_appointment.building_type,
                    'description': new_appointment.description,
                    'date_created': new_appointment.date_created,
                }
            )
            mail_admins(
                "Updateded Inquiry",
                "test...",
                fail_silently=False,
                connection=None,
                html_message=message,
            )
            html_message = loader.render_to_string(
                'emails/client2.html',
                {
                    'subject': 'Thank you, your inquiry has been updated!',
                    'address': new_appointment.address,
                    'building_type': new_appointment.building_type,
                    'description': new_appointment.description,
                }
            )
            send_mail(
                "Inquiry",
                "Thank you, we have received your inquiry. ",
                "oniasnephiisrael@gmail.com",
                [new_appointment.email],
                fail_silently=False,
                html_message=html_message
            )
            return render(request, 'appointments/update.html')
    else:
        form = AppointmentForm(instance=appointment)
        context = { 'form': form }
        return render(request, 'appointments/edit.html', context) 

@login_required
def delete_appointment(request, appointment_id):
    Appointment.objects.get(id=appointment_id).delete()
    return redirect('home')    

def appointment_success(request):
    return render(request, 'appointments/success.html')
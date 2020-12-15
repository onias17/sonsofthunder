from django.shortcuts import render
from django.http import HttpResponse

class Appointments:
    def __init__(self, building, description, address, date):
        self.building = building
        self.description = description
        self.address = address
        self.date = date

appointments = [
    Appointment('Residential', 'need ligthing fixtures installed in the bathroom', '123 Residential Way', '12/20/20'),
    Appointment('Copmmercial', 'need upgraded panels', '456 Commercial Rd', '12/21/20'),
    Appointment('Industrial', 'need electrical ground work to be completed', '789 Industrial Ave', '12/22/20'),
]

# HOME and ABOUT
def home(request):
    return HttpResponse('<h1>Sons of Thunder</h1>')

def about(request):
    return render(request, 'about.html')

# APPOINTMENTS
def appointments(request):
    return render(request, 'appointments/index.html', { 'appointments': appointments })
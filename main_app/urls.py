from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('services/', views.services, name='services'),

    # APPOINTMENT ROUTES
    path('appointments/', views.appointments_index, name='index'),
    path('appointments/<int:appointment_id>/', views.appointments_detail, name='detail'),
    path('appointments/new/', views.add_appointment, name='add_appointment'),
]
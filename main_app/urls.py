from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # APPOINTMENT ROUTES
    path('appointments/', views.appointments_index, name='index'),
    path('appointments/new/', views.add_appointment, name='add_appointment'),
    path('appointments/<int:appointment_id>/', views.appointments_detail, name='detail'),
    path('appointments/<int:appointment_id>/edit/', views.edit_appointment, name='edit_appointment'),
    path('appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),
    path('appointments/success/', views.appointment_success, name='success'),
    path('appointments/update/', views.appointment_update, name='update')
    # AUTH
    
]

urlpatterns += staticfiles_urlpatterns()
from django.shortcuts import render
from .models import TelemedicineAppointment

def telemedicine_appointment_list(request):
    telemedicine_appointments = TelemedicineAppointment.objects.all()
    return render(request, 'telemedicine/telemedicine_appointment_list.html', {'telemedicine_appointments': telemedicine_appointments})

def index(request):
    return render(request, 'index.html')
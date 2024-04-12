from django.http import HttpResponse
from django.shortcuts import render
from .models import Appointment

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Process the form data as needed
        return HttpResponse('Thank you for your message!')

    return render(request, 'contact.html')
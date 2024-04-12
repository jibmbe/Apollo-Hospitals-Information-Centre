from django.db import models

# Create your models here.
class TelemedicineAppointment(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    
    date = models.DateTimeField()
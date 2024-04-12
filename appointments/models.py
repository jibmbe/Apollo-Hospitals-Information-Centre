from django.db import models

# Create your models here.


class Appointment(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    date = models.DateTimeField()
    

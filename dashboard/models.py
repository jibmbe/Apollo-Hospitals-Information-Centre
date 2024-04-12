from django.db import models


class HealthRecord(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)

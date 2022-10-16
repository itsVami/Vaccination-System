from django.shortcuts import render
from django.views.generic import ListView
from .models import Patient

# Patient View

class PatientList(ListView):
    queryset = Patient.objects.all()
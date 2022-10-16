from django.contrib import admin
from .models import Patient

# Patient Admin

class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'name' , 'family' , 'national_code' , 'birth_date' , 'doz1' , 'vaccine' , 'doz2' , 'vaccine2' , 'doz3' , 'vaccine3' , 'doz4' , 'vaccine4' ,
    )

    list_filter = (
        ['birth_date' , 'vaccine' , 'vaccine2' , 'vaccine3' , 'vaccine4' , 'gender']
    )

    search_fields = (
        'name' , 'family' , 'national_code' , 'vaccine' , 'vaccine2' , 'vaccine3' , 'vaccine4' ,
    )

admin.site.register(Patient , PatientAdmin)
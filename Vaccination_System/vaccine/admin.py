from django.contrib import admin
from .models import Vaccine

# Vaccine admin

class VaccineAdmin(admin.ModelAdmin):
    list_display = (
        'name' , 'picture_tag' , 'country' , 'count' , 'is_available' ,
    )

    list_filter = (
        ['country' , 'count' , 'availablity']
    )

    prepopulated_fields = {'slug' : ('name' ,)}   #Auto_Slug

    search_fields = (
        'name' , 'family' , 'national_code' , 'vaccine' ,
    )

    ordering = ['count']

admin.site.register(Vaccine , VaccineAdmin)
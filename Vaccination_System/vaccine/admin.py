from django.contrib import admin
from .models import Vaccine , Category

# Vaccine admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position' ,'title' , 'parent' , 'slug' , 'status') 
    list_filter = (['status'])
    search_fields = ('title' , 'slug')
    prepopulated_fields = {'slug' : ('title' ,)}   #Auto_Slug

admin.site.register(Category , CategoryAdmin)



class VaccineAdmin(admin.ModelAdmin):
    list_display = (
        'name' , 'picture_tag' , 'Category_to_str' , 'country' , 'count' , 'is_available' ,
    )

    list_filter = (
        ['count' , 'country' , 'availablity']
    )

    prepopulated_fields = {'slug' : ('name' ,)}   #Auto_Slug

    search_fields = (
        'name' , 'family' , 'national_code' , 'vaccine' ,
    )

    ordering = ['count']

admin.site.register(Vaccine , VaccineAdmin)
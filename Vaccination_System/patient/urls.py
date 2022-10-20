from django.urls import path , include
from .views import PatientList

app_name = 'patient'
urlpatterns = [
    path('patient/' , PatientList.as_view() , name = 'patients'),
]
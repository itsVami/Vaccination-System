from django.urls import path , include
from .views import PatientList

app_name = 'patient'
urlpatterns = [
    path('' , PatientList.as_view() , name = 'patients')
]
from django.urls import path 
from .views import VaccineList , CategoryList , VaccineDetail

app_name = 'vaccine'
urlpatterns = [
    path('' , VaccineList.as_view() , name = 'vaccines'),
    path('category/<slug:slug>' , CategoryList.as_view() , name='category'),
    path('vaccine/<slug:slug>' , VaccineDetail.as_view() , name='details'),
]   
    
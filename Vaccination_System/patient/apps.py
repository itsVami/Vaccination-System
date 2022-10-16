from django.apps import AppConfig


class PatientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patient'
    verbose_name = 'بیمار'
    verbose_name_plural = 'بیمار ها'
    

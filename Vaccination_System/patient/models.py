from email.policy import default
from itertools import count
from django.db import models
from vaccine.models import Vaccine
from django.utils import timezone
from django.urls import reverse
from jalali_date import date2jalali
from datetime import datetime , timedelta


# My Managers


# My Models

def get_doz2_time():
    return datetime.today() + timedelta(days=21)

def get_doz3_time():
    return datetime.today() + timedelta(days=120)

def get_doz4_time():
    return datetime.today() + timedelta(days=120)
    

class Patient(models.Model):
    STATUS_CHOICES = (
        ('m' , 'مرد'),
        ('f' , 'زن'),
    )

    name = models.CharField(max_length = 150 , verbose_name = 'نام')
    family = models.CharField(max_length = 150 , verbose_name = 'نام خانوادگی')
    national_code = models.CharField(max_length = 10 , verbose_name = 'کد ملی')
    birth_certificate_number = models.CharField(max_length = 10 , verbose_name = 'شماره شناسنامه')
    birth_date = models.DateField(verbose_name = 'تاریخ تولد')
    gender = models.CharField(max_length = 1 , choices = STATUS_CHOICES , verbose_name = 'جنسیت')
    phone_number = models.CharField(max_length = 11 , verbose_name = 'شماره تماس')
    address = models.TextField(max_length = 250 , verbose_name = 'آدرس')
    doz1 = models.BooleanField(default = True , verbose_name = 'دوز اول')
    doz1_time = models.DateField(default=timezone.now , verbose_name = 'تاریخ دریافت دوز اول')
    vaccine = models.ForeignKey(Vaccine , null = True , blank = True , on_delete = models.CASCADE , related_name = 'vaccine1' , verbose_name = 'نام واکسن دوز اول')
    doz2 = models.BooleanField(default = False , verbose_name = 'دوز دوم')
    doz2_time = models.DateField(default=get_doz2_time , verbose_name = 'تاریخ دریافت دوز دوم')
    vaccine2 = models.ForeignKey(Vaccine , null = True , blank = True , on_delete = models.CASCADE , related_name = 'vaccine2' , verbose_name = 'نام واکسن دوز دوم')
    doz3 = models.BooleanField(default = False , verbose_name = 'دوز سوم')
    doz3_time = models.DateField(default=get_doz3_time , verbose_name = 'تاریخ دریافت دوز سوم')
    vaccine3 = models.ForeignKey(Vaccine , null = True , blank = True , on_delete = models.CASCADE , related_name = 'vaccine3' , verbose_name = 'نام واکسن دوز سوم') 
    doz4 = models.BooleanField(default = False , verbose_name = 'دوز چهارم')
    doz4_time = models.DateField(default=get_doz4_time , verbose_name = 'تاریخ دریافت دوز چهارم')
    vaccine4 = models.ForeignKey(Vaccine , null = True , blank = True , on_delete = models.CASCADE , related_name = 'vaccine4' , verbose_name = 'نام واکسن دوز چهارم')


    class Meta :
        verbose_name = 'بیمار'
        verbose_name_plural = 'بیمار ها'
        ordering = ['name' ,'family']


    def __str__(self):
        return self.name  
  
    def get_absolute_url(self):
        return reverse('adminpanel:home')

    def jalali_birth(self):
        return date2jalali(self.birth_date)
    jalali_birth.short_description = "تاریخ تولد" 

    def jalali_doz1(self):
        return date2jalali(self.doz1_time)
    jalali_doz1.short_description = "تاریخ دریافت دوز اول"  

    def jalali_doz2(self):
        return date2jalali(self.doz2_time)
    jalali_doz2.short_description = "تاریخ دریافت دوز دوم"  

    def jalali_doz3(self):
        return date2jalali(self.doz3_time)
    jalali_doz3.short_description = "تاریخ دریافت دوز سوم"  

    def jalali_doz4(self):
        return date2jalali(self.doz4_time)
    jalali_doz4.short_description = "تاریخ دریافت دوز چهارم"   

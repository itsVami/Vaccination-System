from email.policy import default
from itertools import count
from django.db import models
from django.utils.html import format_html

# Vaccine Models

class Vaccine(models.Model):
    name = models.CharField(max_length = 100 , verbose_name = 'نام واکسن')
    slug = models.SlugField(max_length = 100 , unique = True , verbose_name = 'نشانی واکسن')
    country = models.CharField(max_length = 100 , verbose_name = 'کشور تولید کننده')
    count = models.CharField(max_length = 10 , verbose_name = 'تعداد دوز های موجود')
    description = models.TextField(null = True , blank = True , verbose_name ='توضیحات واکسن')
    picture = models.ImageField(upload_to = "images" , default = 'images/vaccine_def.jpg' , verbose_name ='تصویر واکسن')
    availablity = models.BooleanField(default = True , verbose_name ='وضعیت موجودی واکسن')

    def is_available (self):
        if self.count == '0':
            return self.availablity == False
        else:      
            return self.availablity == True
    is_available.boolean = True
    is_available.short_description = 'وضعیت موجودی واکسن'

    class Meta :
        verbose_name = 'واکسن'
        verbose_name_plural = 'واکسن ها'
        ordering = ['count' ,'name']
        
    def __str__(self):
        return self.name 

    def picture_tag(self):
        return format_html("<img width=95 height=80 style='border-radius: 8px;' src='{}'>".format(self.picture.url))
    picture_tag.short_description = "عکس"
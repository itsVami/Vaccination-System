from django.db import models
from django.utils.html import format_html

#My_Managers
class VaccineManager(models.Manager):
    def available (self):
        return self.filter(availablity = True)


class CategoryManager(models.Manager):
    def active (self):
        return self.filter(status = True)

# Vaccine Models

class Category (models.Model):
    title = models.CharField(max_length=200 , verbose_name ='عنوان دسته بندی')
    slug = models.SlugField(max_length=100 , unique=True , verbose_name ='آدرس دسته یندی')
    parent = models.ForeignKey('self' , default = None , null = True , blank = True , on_delete = models.SET_NULL , related_name = 'children' , verbose_name = 'زیر دسته')
    status = models.BooleanField(verbose_name ='انتشار داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن دسته بندی') 
   
    class Meta :
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id' ,'position']
    
    def __str__(self):
        return self.title

    objects = CategoryManager()



class Vaccine(models.Model):
    name = models.CharField(max_length = 100 , verbose_name = 'نام واکسن')
    slug = models.SlugField(max_length = 100 , unique = True , verbose_name = 'نشانی واکسن')
    country = models.CharField(max_length = 100 , verbose_name = 'کشور تولید کننده')
    count = models.CharField(max_length = 10 , verbose_name = 'تعداد دوز های موجود')
    description = models.TextField(null = True , blank = True , verbose_name ='توضیحات واکسن')
    picture = models.ImageField(upload_to = "images" , default = 'images/vaccine_def.jpg' , verbose_name ='تصویر واکسن')
    availablity = models.BooleanField(default = True , verbose_name ='وضعیت موجودی واکسن')
    category = models.ManyToManyField(Category , related_name="vaccines" , verbose_name='دسته بندی')

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

    def Category_to_str(self):
        return " , ".join([category.title for category in self.category.active()])
    Category_to_str.short_description = "دسته بندی"

    objects = VaccineManager()
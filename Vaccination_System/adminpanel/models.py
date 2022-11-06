from django.db import models
from django.contrib.auth.models import AbstractUser

# My Models

class Admin(AbstractUser):
    email = models.EmailField(unique=True , verbose_name='ایمیل' )
    profile_avatar = models.ImageField(upload_to="Profile" , default="Profile/default_avatar.png" , verbose_name='عکس پروفایل')
    is_author = models.BooleanField(default=True , verbose_name='ادمین')
    special_user = models.BooleanField (default=False , verbose_name ='کاربر ویژه')
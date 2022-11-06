# Generated by Django 4.1.2 on 2022-11-04 16:25

from django.db import migrations, models
import patient.models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0016_alter_patient_doz2_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doz3_time',
            field=models.DateField(default=patient.models.get_doz3_time, verbose_name='تاریخ دریافت دوز سوم'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doz4_time',
            field=models.DateField(default=patient.models.get_doz4_time, verbose_name='تاریخ دریافت دوز چهارم'),
        ),
    ]

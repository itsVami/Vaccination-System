# Generated by Django 4.1.2 on 2022-11-02 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_alter_patient_doz2_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doz2_time',
            field=models.DateField(default=datetime.datetime(2022, 12, 2, 19, 26, 39, 854856), verbose_name='تاریخ دریافت دوز دوم'),
        ),
    ]

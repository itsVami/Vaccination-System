# Generated by Django 4.1.2 on 2022-10-16 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_birth_certificate_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'بیمار', 'verbose_name_plural': 'بیمار ها'},
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='family',
            new_name='last_name',
        ),
    ]

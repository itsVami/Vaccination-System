# Generated by Django 4.1.2 on 2022-10-16 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_patient_options_rename_name_patient_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['name', 'family'], 'verbose_name': 'بیمار', 'verbose_name_plural': 'بیمار ها'},
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='last_name',
            new_name='family',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='first_name',
            new_name='name',
        ),
    ]

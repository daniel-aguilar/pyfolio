# Generated by Django 3.2.13 on 2022-04-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0008_alter_patient_identification'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

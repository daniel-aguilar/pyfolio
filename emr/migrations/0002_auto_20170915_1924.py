# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 19:24
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_condition', models.TextField(verbose_name='Current Condition')),
                ('current_treatment', models.TextField(verbose_name='Current Treatment')),
                ('reference', models.TextField(verbose_name='Reference')),
                ('physical_exploration', models.TextField(verbose_name='Physical Exploration')),
                ('diagnosis', models.TextField(verbose_name='Diagnosis')),
                ('treatment_to_follow', models.TextField(verbose_name='Treatment to Follow')),
                ('additional_notes', models.TextField(verbose_name='Additional Notes')),
            ],
            options={
                'verbose_name': 'Medical Record',
                'verbose_name_plural': 'Medical Records',
            },
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=45, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='identification',
            field=models.CharField(max_length=9, verbose_name='Identification'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=45, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.CharField(max_length=45, verbose_name='Occupation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=8, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.IntegerField(choices=[(0, 'Not Known'), (1, 'Male'), (2, 'Female'), (9, 'Not Applicable')], default=0, verbose_name='Sex'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medical_record', to='emr.Patient'),
        ),
    ]

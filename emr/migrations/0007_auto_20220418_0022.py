# Generated by Django 3.2.13 on 2022-04-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0006_auto_20171118_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

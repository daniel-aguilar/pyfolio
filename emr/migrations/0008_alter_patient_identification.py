# Generated by Django 3.2.13 on 2022-04-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0007_auto_20220418_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='identification',
            field=models.CharField(max_length=20, unique=True, verbose_name='Identification'),
        ),
    ]

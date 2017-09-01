from django.db import models

# Create your models here.

class Patient(models.Model):
    identification = models.CharField(max_length=9)
    date_added = models.DateTimeField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    sex = models.IntegerField()
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=8)
    address = models.TextField()

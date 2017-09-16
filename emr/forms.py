from django.forms import ModelForm

from .models import MedicalRecord


class MedicalRecordForm(ModelForm):

    class Meta:
        model = MedicalRecord
        exclude = ['patient']

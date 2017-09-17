from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Patient(models.Model):

    NOT_KNOWN = 0
    MALE = 1
    FEMALE = 2
    NOT_APPLICABLE = 9

    SEX_CHOICES = [
        (NOT_KNOWN, _('Not Known')),
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (NOT_APPLICABLE, _('Not Applicable')),
    ]

    identification = models.CharField(
        _('Identification'),
        max_length=9,
        unique=True
    )
    date_added = models.DateTimeField(_('Date Added'), auto_now_add=True)
    first_name = models.CharField(_('First Name'), max_length=45)
    last_name = models.CharField(_('Last Name'), max_length=45)
    sex = models.IntegerField(_('Sex'), choices=SEX_CHOICES, default=NOT_KNOWN)
    date_of_birth = models.DateField(_('Date of Birth'))
    occupation = models.CharField(_('Occupation'), max_length=45)
    phone_number = models.CharField(_('Phone Number'), max_length=8)
    address = models.TextField(_('Address'))

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')

    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def sex_verbose(self):
        return dict(self.SEX_CHOICES)[self.sex]

    def age(self):
        return relativedelta(datetime.now(), self.date_of_birth).years

    def has_medical_record(self):
        return hasattr(self, 'medical_record')

    def __str__(self):
        return self.full_name()


class MedicalRecord(models.Model):

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_record'
    )
    current_condition = models.TextField(_('Current Condition'))
    current_treatment = models.TextField(_('Current Treatment'))
    reference = models.TextField(_('Reference'))
    physical_exploration = models.TextField(_('Physical Exploration'))
    diagnosis = models.TextField(_('Diagnosis'))
    treatment_to_follow = models.TextField(_('Treatment to Follow'))
    additional_notes = models.TextField(_('Additional Notes'), blank=True)

    class Meta:
        verbose_name = _('Medical Record')
        verbose_name_plural = _('Medical Records')

    def __str__(self):
        return _("%(patient_full_name)s's Medical Record") % {'patient_full_name': self.patient.full_name()}
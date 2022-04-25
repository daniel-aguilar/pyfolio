from datetime import date
from uuid import uuid4

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def patient_profile_picture_path(instance, filename):
    return 'profile_pictures/{0}'.format(str(uuid4()))


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
    profile_picture = models.ImageField(
        _('Profile Picture'),
        upload_to=patient_profile_picture_path,
        blank=True,
    )
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

        ordering = ['id']

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def sex_verbose(self):
        return dict(self.SEX_CHOICES)[self.sex]

    def age(self):
        return relativedelta(date.today(), self.date_of_birth).years

    def has_medical_record(self):
        return hasattr(self, 'medical_record')

    def has_profile_picture(self):
        return bool(self.profile_picture)

    def clean(self):
        if self.date_of_birth > date.today():
            raise ValidationError({'date_of_birth': _('Invalid date of birth.')})


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
        db_table = 'emr_medical_record'
        verbose_name = _('Medical Record')
        verbose_name_plural = _('Medical Records')

    def __str__(self):
        return _("%(patient_full_name)s's Medical Record") % {'patient_full_name': self.patient.full_name()}

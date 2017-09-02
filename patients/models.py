from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Patient(models.Model):

    # Sex choices
    NOT_KNOWN = 0
    MALE = 1
    FEMALE = 2
    NOT_APPLICABLE = 9

    SEX_CHOICES = (
        (NOT_KNOWN, _('Not Known')),
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (NOT_APPLICABLE, _('Not Applicable')),
    )

    identification = models.CharField(_('Identification'), max_length=9)
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

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

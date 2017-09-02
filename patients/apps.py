from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PatientsConfig(AppConfig):
    name = 'patients'
    verbose_name = _('Patients')

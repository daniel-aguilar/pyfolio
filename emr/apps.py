from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class EMRConfig(AppConfig):
    name = 'emr'
    verbose_name = _('EMR')

    def ready(self):
        from .signals import patient_file_handler

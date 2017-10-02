from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Patient


@receiver(post_delete, sender=Patient)
def patient_file_handler(sender, instance, **kwargs):
    if instance.profile_picture:
        instance.profile_picture.delete(False)

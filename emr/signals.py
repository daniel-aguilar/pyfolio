from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from PIL import Image

from .models import Patient


@receiver(pre_save, sender=Patient)
def clear_previous_image_handler(instance, **kwargs):
    if not instance.profile_picture:
        try:
            pre = Patient.objects.get(pk=instance.pk)
            pre.profile_picture.delete(False)
        except Patient.DoesNotExist:
            pass


@receiver(post_save, sender=Patient)
def compress_image_handler(instance, **kwargs):
    if instance.profile_picture:
        path = instance.profile_picture.path
        img = Image.open(path)
        img.save(path, format="JPEG", quality=20, optimize=True)


@receiver(post_delete, sender=Patient)
def patient_file_handler(sender, instance, **kwargs):
    if instance.profile_picture:
        instance.profile_picture.delete(False)

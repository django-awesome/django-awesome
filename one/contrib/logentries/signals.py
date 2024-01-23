from django.contrib.admin.models import LogEntry
from django.db.models.signals import post_save
from django.dispatch import receiver

from .decorators import logentry_processing


@receiver(post_save, sender=LogEntry)
@logentry_processing()
def logentry_receiver(sender, **kwargs):  # pragma: no cover
    pass

from django.contrib.auth import get_user_model
from django_guid import get_guid

from config import celery_app

from .models import LogDetail
from .serializers import serializer_data

User = get_user_model()


@celery_app.task()
def initial_snapshot(logentry_id, context=None):
    log_detail, _ = LogDetail.objects.get_or_create(logentry_id=logentry_id)
    instance = log_detail.logentry.get_edited_object()
    snapshot = serializer_data(instance=instance)
    log_detail.snapshot = snapshot
    log_detail.uid = get_guid()
    log_detail.metadata = context
    log_detail.save()
    return log_detail


@celery_app.task()
def final_snapshot(logentry_id, snapshot, context=None):
    log_detail, _ = LogDetail.objects.get_or_create(logentry_id=logentry_id)
    log_detail.snapshot = snapshot
    log_detail.metadata = context
    log_detail.uid = get_guid()
    log_detail.save()

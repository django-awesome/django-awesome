from django.contrib.admin.models import LogEntry
from django.db.models import CASCADE, CharField, JSONField, Model, OneToOneField
from django.utils.translation import gettext_lazy as _


class LogDetail(Model):
    logentry = OneToOneField(LogEntry, on_delete=CASCADE, related_name="detail")
    uid = CharField(_("UID"), max_length=50, blank=True, null=True)
    metadata = JSONField(_("Meta"), default=dict, blank=True, null=True)
    snapshot = JSONField(_("Snapshot"), default=dict, blank=True, null=True)
    diffs = JSONField(_("Different with previous version"), default=list, blank=True, null=True)

    class Meta:
        verbose_name = _("log detail")
        verbose_name_plural = _("log details")
        db_table = "django_admin_log_detail"

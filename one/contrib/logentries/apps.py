from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LogEntryConfig(AppConfig):
    name = "one.contrib.logentries"
    verbose_name = _("Django Log Entries")

    def ready(self):
        try:
            import one.contrib.logentries.signals  # noqa F401
        except ImportError:  # pragma: no cover
            pass

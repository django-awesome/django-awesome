from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdminDashboardConfig(AppConfig):
    name = "one.contrib.admin.dashboard"
    verbose_name = _("Admin Dashboard")

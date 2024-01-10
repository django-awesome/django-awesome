from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdminMenuConfig(AppConfig):
    name = "one.contrib.admin.menu"
    verbose_name = _("Admin Menu")

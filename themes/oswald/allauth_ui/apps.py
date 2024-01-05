from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OswaldAllauthConfig(AppConfig):
    name = "themes.oswald.allauth_ui"
    verbose_name = _("Oswald Theme")

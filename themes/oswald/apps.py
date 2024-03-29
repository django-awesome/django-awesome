from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OswaldThemeConfig(AppConfig):
    name = "themes.oswald"
    verbose_name = _("Oswald Theme")

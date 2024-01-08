from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GrappelliTestConfig(AppConfig):
    name = "one.libraries.grappelli.grappelli_test"
    verbose_name = _("Grappelli Test")

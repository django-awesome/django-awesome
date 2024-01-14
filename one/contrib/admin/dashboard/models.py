from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class DashboardPreferences(models.Model):
    """
    This model represents the dashboard preferences for a user.
    """

    user = models.ForeignKey(User, verbose_name=_("User dashboard preferences"), on_delete=models.CASCADE)
    code = models.CharField(_("Dashboard Code"), max_length=100)
    data = models.TextField(_("Dashboard Data"), blank=True, null=True)

    class Meta:
        db_table = "dashboard_preferences"
        verbose_name = _("Dashboard preference")
        verbose_name_plural = _("Dashboard preferences")
        unique_together = (
            "user",
            "code",
        )
        ordering = ("user",)

    def __str__(self):
        return f"{self.user} {self.code}"

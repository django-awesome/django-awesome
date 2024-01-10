from django.contrib.auth import get_user_model
from django.db.models import CASCADE, CharField, ForeignKey, Model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Bookmark(Model):
    """
    This model represents a user created bookmark.
    """

    user = ForeignKey(User, verbose_name=_("Belong to user"), on_delete=CASCADE)
    url = CharField(_("Bookmark url"), max_length=255)
    title = CharField(_("Bookmark title"), max_length=255)
    description = CharField(_("Bookmark description"), max_length=255, blank=True, null=True)
    icon = TextField(_("Bookmark icon"), blank=True, default="")

    class Meta:
        verbose_name = _("Bookmark Menu")
        verbose_name_plural = _("Bookmark Menus")
        ordering = ("id",)

    def __str__(self):
        return f"{self.title}"

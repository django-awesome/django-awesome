from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from one.users.utils import user_directory_path


class User(AbstractUser):
    """
    Default custom user model for Django Awesome.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    avatar = ImageField(
        _("Avatar"),
        upload_to=user_directory_path,
        blank=True,
        null=True,
        help_text=_("Allowed file types:  png, jpg, jpeg."),
    )

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

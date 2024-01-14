from django.forms import ModelForm

from .models import DashboardPreferences


class DashboardPreferencesForm(ModelForm):
    """
    This form allows the user to edit dashboard preferences. It doesn't show
    the user field. It expects the user to be passed in from the view.
    """

    class Meta:
        fields = ("data",)
        model = DashboardPreferences

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.code = kwargs.pop("code", None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        preference = super().save(commit=False, *args, **kwargs)
        preference.user = self.user
        preference.code = self.code
        preference.save()
        return preference

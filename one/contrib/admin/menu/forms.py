from django.contrib.admin.utils import unquote
from django.forms import ModelForm

from .models import Bookmark


class BookmarkForm(ModelForm):
    """
    This form allows users to edit bookmarks. It doesn't show the user field.
    It expects the user to be passed in from the view.
    """

    class Meta:
        fields = ("url", "title", "description", "icon")
        model = Bookmark

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_url(self):
        return unquote(self.cleaned_data["url"])

    def save(self, *args, **kwargs):
        bookmark = super().save(commit=False, *args, **kwargs)
        bookmark.user = self.user
        bookmark.save()
        return bookmark

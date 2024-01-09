from django.urls import path

from .views import add_bookmark, remove_bookmark

urlpatterns = [
    path("add_bookmark/", add_bookmark, name="admin-menu-add-bookmark"),
    path("remove_bookmark/<int:id>/", remove_bookmark, name="admin-menu-remove-bookmark"),
]

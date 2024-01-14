from django.urls import path

from .views import set_preferences

urlpatterns = [
    path("set_preferences/<str:code>/", set_preferences, name="admin-dashboard-set-preferences"),
]

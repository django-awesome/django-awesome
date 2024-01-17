from django.conf import settings


def dashboard_settings(request):
    """Expose some settings from django-allauth in templates."""
    return {
        "DASHBOARD_ENABLE": getattr(settings, "DASHBOARD_ENABLE", False),
    }

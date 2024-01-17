from .dashboards import Dashboard, dashboard
from .decorators import register_to_dashboard
from .modules import BaseModule

__all__ = ["autodiscover", "BaseModule", "dashboard", "Dashboard", "register_to_dashboard"]


def autodiscover(blacklist=[]):
    import imp
    from importlib import import_module

    from django.conf import settings

    blacklist.append("one.contrib.admin.dashboard")
    blacklist.append("one.contrib.admin.menu")

    for app in settings.INSTALLED_APPS:
        # skip blacklisted apps
        if app in blacklist:
            continue

        # try to import the app
        try:
            app_path = import_module(app).__path__
        except AttributeError:
            continue

        # try to find a app.dashboard module
        try:
            imp.find_module("dashboard", app_path)
        except ImportError:
            continue

        # looks like we found it so import it!
        import_module("%s.dashboard" % app)

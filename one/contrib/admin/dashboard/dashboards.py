from django.template.defaultfilters import slugify
from django.utils.encoding import force_str
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string


class Dashboard:
    registry = {}
    columns = 2

    class Media:
        css = ()
        js = ()

    @staticmethod
    def get_code(context):
        app_label = context.get("app_label", None)
        if app_label:
            return f"{slugify(force_str(app_label))}-dashboard"
        return "dashboard"

    def register(self, klass):
        from .modules import BaseModule

        if not issubclass(klass, BaseModule):
            raise ValueError(f"{klass} is not an instance of Dashboard Module")
        if klass in self.registry:
            raise ValueError(f"{klass} is already registered in Dashboard")
        klass_instance = klass()
        self.registry[klass_instance.id] = klass_instance


class DefaultDashboard(LazyObject):
    def _setup(self):
        DashboardClass = import_string("one.contrib.admin.dashboard.Dashboard")  # noqa
        self._wrapped = DashboardClass()

    def __repr__(self):
        return repr(self._wrapped)


# This global object represents the default dashboard, for the common case.
# You can also instantiate AdminSite in your own code to create a custom dashboard.
dashboard = DefaultDashboard()

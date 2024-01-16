"""
Dashboard template tags, the following dashboard tags are available:

 * ``{% admin_render_dashboard %}``
 * ``{% admin_render_dashboard_module %}``

To load the dashboard tags in your templates: ``{% load admin_dashboard_tags %}``.
"""

from django import template

from ..dashboards import dashboard
from ..models import DashboardPreferences as Preference

register = template.Library()


@register.inclusion_tag("dashboard/dashboard.html", takes_context=True)
def admin_render_dashboard(context):
    dashboard_code = dashboard.get_code(context)

    preference, _ = Preference.objects.get_or_create(user=context["request"].user, code=dashboard_code)

    context.update(
        {
            "dashboard": dashboard,
            "dashboard_code": dashboard_code,
            "preferences": sorted(preference.data, key=lambda x: preference.data[x].get("order", 0)),
        }
    )

    return context


@register.inclusion_tag("dashboard/dummy.html", takes_context=True)
def admin_render_dashboard_module(context, module):
    module.init_with_context(context)

    context.update(
        {
            "template": module.template,
            "module": module,
        }
    )

    return context


@register.filter
def get_module_by_id(registry, key):
    return registry.get(key)

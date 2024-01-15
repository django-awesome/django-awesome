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

    dashboard_preferences, _ = Preference.objects.get_or_create(user=context["request"].user, code=dashboard_code)

    context.update(
        {
            "dashboard": dashboard,
            "dashboard_preferences": dashboard_preferences,
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

"""
Menu template tags, the following menu tags are available:

 * ``{% admin_render_menu %}``
 * ``{% admin_render_menu_item %}``
 * ``{% admin_render_menu_css %}``

To load the menu tags in your templates: ``{% load admin_menu_tags %}``.
"""

from django import template
from django.contrib import admin
from django.urls import reverse

from ..items import Bookmarks
from ..menus import Menu as DefaultMenu
from ..models import Bookmark

register = template.Library()
tag_func = register.inclusion_tag("menu/dummy.html", takes_context=True)


def admin_render_menu(context):
    """
    Template tag that renders the menu, it takes an optional ``Menu`` instance
    as unique argument, if not given, the menu will be retrieved with the
    ``get_admin_menu`` function.
    """
    menu = DefaultMenu()
    menu.init_with_context()
    has_bookmark_item = False
    bookmark = None
    if len([c for c in menu.children if isinstance(c, Bookmarks)]) > 0:
        has_bookmark_item = True
        url = context["request"].get_full_path()
        try:
            bookmark = Bookmark.objects.filter(user=context["request"].user, url=url)[0]
        except:  # noqa
            pass

    context.update(
        {
            "template": menu.template,
            "menu": menu,
            "has_bookmark_item": has_bookmark_item,
            "bookmark": bookmark,
            "admin_url": reverse("%s:index" % admin.site.name),
        }
    )
    return context


admin_render_menu = tag_func(admin_render_menu)


def admin_render_menu_item(context, item, template=None, index=None):
    """
    Template tag that renders a given menu item, it takes a ``MenuItem``
    instance as unique parameter.
    """
    item.init_with_context(context)

    context.update(
        {
            "template": template if template else item.template,
            "item": item,
            "index": index,
            "selected": item.is_selected(context["request"]),
            "admin_url": reverse(f"{admin.site.name}:index"),
        }
    )
    return context


admin_render_menu_item = tag_func(admin_render_menu_item)


def admin_render_menu_css(context, menu=None):
    """
    Template tag that renders the menu css files, it takes an optional
    ``Menu`` instance as unique argument, if not given, the menu will be
    retrieved with the ``get_admin_menu`` function.
    """
    if menu is None:
        menu = DefaultMenu()

    context.update(
        {
            "template": "menu/css.html",
            "css_files": menu.Media.css,
        }
    )
    return context


admin_render_menu_css = tag_func(admin_render_menu_css)

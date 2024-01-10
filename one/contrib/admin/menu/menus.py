from django.utils.translation import gettext_lazy as _

from .items import AppList, Bookmarks


class Menu:
    """
    This is the base class for creating custom navigation menus.
    A menu can have the following properties:

    ``template``
        A string representing the path to template to use to render the menu.
        As for any other template, the path must be relative to one of the
        directories of your ``TEMPLATE_DIRS`` setting.
        Default value: "admin_tools/menu/menu.html".

    ``children``
        A list of children menu items. All children items mus be instances of
        the :class:`~admin_tools.menu.items.MenuItem` class.

    If you want to customize the look of your menu and it's menu items, you
    can declare css stylesheets and/or javascript files to include when
    rendering the menu, for example::

        from admin_tools.menu import Menu

        class MyMenu(Menu):
            class Media:
                css = {'all': ('css/mymenu.css',)}
                js = ('js/mymenu.js',)
    """

    template = "menu/menu.html"
    children = None

    class Media:
        css = ()
        js = ()

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])
        self.children = kwargs.get("children", [])

    def init_with_context(self):
        self.children += [
            AppList(_("Applications"), exclude=("django.contrib.*",)),
            AppList(_("Administration"), models=("django.contrib.*",)),
            Bookmarks(),
        ]

"""
    Base class for all dashboard modules.
    Dashboard modules have the following properties:

    ``enabled``
        Boolean that determines whether the module should be enabled in
        the dashboard by default or not. Default value: ``True``.

    ``draggable``
        Boolean that determines whether the module can be draggable or not.
        Draggable modules can be re-arranged by users. Default value: ``True``.

    ``collapsible``
        Boolean that determines whether the module is collapsible, this
        allows users to show/hide module content. Default: ``True``.

    ``deletable``
        Boolean that determines whether the module can be removed from the
        dashboard by users or not. Default: ``True``.

    ``title``
        String that contains the module title, make sure you use the django
        gettext functions if your application is multilingual.
        Default value: ''.

    ``title_url``
        String that contains the module title URL. If given the module
        title will be a link to this URL. Default value: ``None``.

    ``css_classes``
        A list of css classes to be added to the module ``div`` class
        attribute. Default value: ``None``.

    ``pre_content``
        Text or HTML content to display above the module content.
        Default value: ``None``.

    ``content``
        The module text or HTML content. Default value: ``None``.

    ``post_content``
        Text or HTML content to display under the module content.
        Default value: ``None``.

    ``template``
        The template to use to render the module.
        Default value: 'admin_tools/dashboard/module.html'.
"""


class BaseModule:
    id = None
    template = None
    title = ""
    title_url = None
    css_classes = None
    pre_content = None
    post_content = None
    children = None
    enabled = True
    draggable = True
    collapsible = True
    deletable = True
    show_title = True

    def __init__(self, title=None, **kwargs):
        self.id = self.id or self.__class__.__name__.lower()
        if title is not None:
            self.title = title

        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])

        self.children = self.children or []
        self.css_classes = self.css_classes or []
        # boolean flag to ensure that the module is initialized only once
        self._initialized = False

    def init_with_context(self, context):
        """
        if self._initialized:
            return

        self._initialized = True
        """
        pass

    def is_empty(self):
        return self.pre_content is None and self.post_content is None and len(self.children) == 0

    def render_css_classes(self):
        ret = ["dashboard-module"]
        if not self.enabled:
            ret.append("disabled")
        if self.draggable:
            ret.append("draggable")
        if self.collapsible:
            ret.append("collapsible")
        if self.deletable:
            ret.append("deletable")
        ret += self.css_classes
        return " ".join(ret)

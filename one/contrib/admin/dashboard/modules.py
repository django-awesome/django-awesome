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
    icon = None
    title = None
    title_url = None
    description = None
    css_classes = None
    custom_style = None
    children = None

    def __init__(self, **kwargs):
        self.id = self.id or self.__class__.__name__.lower()

        class_name = self.__class__.__name__

        if not self.template:
            raise NotImplementedError("You must specify a template for the module %s" % class_name)

        if not self.title:
            raise NotImplementedError(f"You must specify a title for the module {class_name}")

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

    def render_css_classes(self):
        ret = []
        if self.css_classes:
            ret += self.css_classes
        return " ".join(ret)

    def render_custom_style(self):
        ret = []
        if self.custom_style:
            ret += self.custom_style
        return "; ".join(ret)

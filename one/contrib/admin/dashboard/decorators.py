def register_to_dashboard(register_to=None):
    def _dashboard_module_wrapper(module):
        if not register_to:
            from .dashboards import dashboard

            dashboard.register(module)
        else:
            register_to.register(module)
        return module

    return _dashboard_module_wrapper

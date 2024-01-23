import logging

from .context import set_request_context

logger = logging.getLogger(__name__)


class LogEntryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        set_request_context(request)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response

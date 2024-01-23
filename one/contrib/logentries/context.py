from django.core.cache import cache
from django_guid import get_guid


def get_context():
    return cache.get(get_guid())


def set_context(data):
    cache.set(get_guid(), data, timeout=3600)


def set_request_context(request):
    context = get_context()
    _request = {
        "path": request.path,
        "method": request.method,
        "body": request.body.decode("utf-8"),
        "headers": dict(request.headers),
        "query_params": dict(request.GET),
    }
    if not context:
        set_context({"request": _request})
    else:
        context["request"] = _request
        set_context(context)


def clear_context():
    cache.delete(get_guid())

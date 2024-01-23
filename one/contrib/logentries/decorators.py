import logging
import time

from django.contrib.admin.models import ADDITION, CHANGE, DELETION

from .context import get_context
from .serializers import serializer_data
from .tasks import final_snapshot, initial_snapshot

logger = logging.getLogger("data")


def logentry_processing():
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            sender = kwargs.get("sender", None)
            logentry = kwargs.get("instance")
            action_flag = logentry.action_flag
            context = get_context()
            if action_flag in [ADDITION, CHANGE]:
                initial_snapshot.delay(logentry.id, context)
            elif action_flag == DELETION:
                instance = logentry.get_edited_object()
                data = serializer_data(instance)
                final_snapshot.delay(logentry.id, data, context)

            str_execute_time = f"{time.time() - start:.10f}"
            print(f"Model: {sender.__name__}, Time: {str_execute_time}")

            return func(*args, **kwargs)

        return wrapper

    return decorator

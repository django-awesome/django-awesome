import json

from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import DashboardPreferencesForm
from .models import DashboardPreferences


@staff_member_required
@csrf_exempt
def set_preferences(request, code):
    preference = get_object_or_404(DashboardPreferences, user=request.user, code=code)
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        if data == {}:
            preference.data = {}
            preference.save()
            return JsonResponse({"status": "ok"}, status=200)

        form = DashboardPreferencesForm(user=request.user, code=code, data={"data": data}, instance=preference)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "ok"}, status=200)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "server error"}, status=400)

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
    if request.headers.get("x-requested-with") == "XMLHttpRequest" and request.method == "POST":
        form = DashboardPreferencesForm(user=request.user, code=code, data=request.POST, instance=preference)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "ok"}, status=200)
        else:
            return JsonResponse({"status": "error"}, status=400)

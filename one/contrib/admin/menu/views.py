from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from .forms import BookmarkForm
from .models import Bookmark


@staff_member_required
@csrf_exempt
def add_bookmark(request):
    if not request.headers.get("x-requested-with") == "XMLHttpRequest" and request.method == "POST":
        form = BookmarkForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Bookmark added"))
            if request.POST.get("next"):
                return HttpResponseRedirect(request.POST.get("next"))

    return HttpResponseRedirect(f"/{settings.ADMIN_URL}")


@staff_member_required
@csrf_exempt
def remove_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, id=id, user=request.user)
    if not request.headers.get("x-requested-with") == "XMLHttpRequest" and request.method == "POST":
        bookmark.delete()
        messages.success(request, _("Bookmark removed"))
        if request.POST.get("next"):
            return HttpResponseRedirect(request.POST.get("next"))

    return HttpResponseRedirect(f"/{settings.ADMIN_URL}")

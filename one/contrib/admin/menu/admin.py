from django.contrib import admin

from .models import Bookmark


@admin.register(Bookmark)
class AdminBookmarkOption(admin.ModelAdmin):
    list_display = ("title", "url", "description")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(user=request.user)

    def get_changeform_initial_data(self, request):
        init_data = super().get_changeform_initial_data(request)
        init_data["user"] = request.user
        return init_data

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            return readonly_fields + ("user",)
        else:
            return readonly_fields

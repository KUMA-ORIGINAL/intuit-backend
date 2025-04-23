from django.contrib import admin
from import_export.admin import ExportActionModelAdmin

from university_additions.models.user_application import UserApplication


@admin.register(UserApplication)
class UserApplicationAdmin(ExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["user", "phone", "email", "slug", "created", "status"]
    readonly_fields = ("user", "phone", "email", "slug", "created")
    list_filter = ("slug", "status")
    ordering = ('-created',)
    list_editable = ("status",)

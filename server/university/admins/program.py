from django.contrib import admin
from django.utils.safestring import mark_safe

from university.models.program import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', "get_photo"]
    search_fields = ["title"]
    list_filter = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    list_per_page = 20
    readonly_fields = ["get_photo"]

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=80>")

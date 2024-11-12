from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

from university.models.faculty import Faculty


@admin.register(Faculty)
class FacultyAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title', "get_photo"]
    list_display_links = ['id', 'title',]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    list_per_page = 20
    readonly_fields = ["get_photo"]

    def get_photo(self, object):
        if object.banner:
            return mark_safe(f"<img src='{object.banner.url}' height=80>")

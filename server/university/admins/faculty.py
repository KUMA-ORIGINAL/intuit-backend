from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedTranslationAdmin

from university.models.faculty import Faculty


@admin.register(Faculty)
class FacultyAdmin(TabbedTranslationAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": CKEditorWidget,
        }
    }
    list_display = ['id', 'title', 'get_icon', "get_banner"]
    list_display_links = ['id', 'title',]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    list_per_page = 20
    readonly_fields = ['get_icon', "get_banner"]

    def get_banner(self, obj):
        if obj.banner:
            return mark_safe(f"<img src='{obj.banner.url}' width='100px' style='height: auto;'>")
        return ''

    get_banner.short_description = 'Баннер'

    def get_icon(self, obj):
        if obj.icon:
            return mark_safe(f"<img src='{obj.icon.url}' width='100px' style='height: auto;'>")
        return ''

    get_icon.short_description = 'Иконка'
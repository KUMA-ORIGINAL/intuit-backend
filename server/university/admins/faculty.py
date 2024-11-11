from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from university.models.faculty import Faculty


@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ['id', 'title', "get_photo"]
    list_display_links = ['id', 'title',]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    list_per_page = 20
    readonly_fields = ["get_photo"]

    def get_photo(self, object):
        if object.banner:
            return mark_safe(f"<img src='{object.banner.url}' height=80>")

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
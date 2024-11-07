from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from university.models.staff import Position, Staff


@admin.register(Position)
class PositionAdmin(TranslationAdmin):
    list_display = ['id', "title", "level"]
    list_editable = ["level"]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Staff)
class StaffAdmin(TranslationAdmin):
    search_fields   = ["name" ]
    prepopulated_fields = {"slug": ["name"]}
    list_display = ['id', 'name', 'get_photo', "position"]
    list_filter = ["position", "name"]
    list_editable = ["position"]
    list_per_page = 20
    filter_horizontal = ["faculty"]

    readonly_fields = ["get_photo"]
    save_as = True

    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=100>")
    get_photo.short_description = "Фото"

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
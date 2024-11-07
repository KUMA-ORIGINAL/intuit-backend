from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from university_additions.models.partner import Partner


@admin.register(Partner)
class PartnerAdmin(TranslationAdmin):
    list_display = ['title', 'get_logo']
    readonly_fields = ["get_logo"]
    search_fields = ["title"]
    filter_horizontal = ["faculty"]

    def get_logo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' height=100>")

    get_logo.short_description = "логотип"

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
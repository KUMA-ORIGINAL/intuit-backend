from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from university.models import Detail


@admin.register(Detail)
class DetailAdmin(TranslationAdmin):
    list_display = ["id", "title", 'subtitle']
    list_display_links = ["id"]
    search_fields = ["title", "subtitle"]
    list_per_page = 20

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
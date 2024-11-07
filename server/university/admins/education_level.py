from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from university.models.education_level import EducationLevel, AdmissionEligibility


@admin.register(AdmissionEligibility)
class AdmissionEligibilityAdmin(TranslationAdmin):
    list_display = ['id', 'name']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(EducationLevel)
class EducationLevelAdmin(TranslationAdmin):
    list_display = ['id', 'title', "get_photo"]
    search_fields = ["title"]
    list_filter = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    list_per_page = 20
    readonly_fields = ["get_photo"]

    def get_photo(self, object):
        if object.banner:
            return mark_safe(f"<img src='{object.banner.url}' height=80>")

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
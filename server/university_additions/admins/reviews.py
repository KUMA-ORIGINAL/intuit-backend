from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from university_additions.models.reviews import StudentReview, StudentSpeak


@admin.register(StudentReview)
class StudentReviewAdmin(TranslationAdmin):
    list_display = ['name', 'get_photo']
    readonly_fields = ["get_photo"]
    search_fields = ["name"]
    filter_horizontal = [ "faculty", 'education_level' ]

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=80>")

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(StudentSpeak)
class StudentSpeakAdmin(TranslationAdmin):
    list_display = ['name', 'get_photo']
    readonly_fields = ["get_photo"]
    search_fields = ["name"]
    filter_horizontal = [ "faculty", 'education_level' ]

    def get_photo(self, object):
        if object.preview:
            return mark_safe(f"<img src='{object.preview.url}' height=80>")

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
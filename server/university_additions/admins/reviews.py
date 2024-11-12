from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedTranslationAdmin

from university_additions.models.reviews import StudentReview, StudentSpeak


@admin.register(StudentReview)
class StudentReviewAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'name', 'get_photo']
    list_display_links = ['id', 'name']
    readonly_fields = ["get_photo"]
    search_fields = ["name"]
    filter_horizontal = [ "faculty", 'education_level' ]

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=80>")


@admin.register(StudentSpeak)
class StudentSpeakAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'name', 'get_photo']
    list_display_links = ['id', 'name']
    readonly_fields = ["get_photo"]
    search_fields = ["name"]
    filter_horizontal = [ "faculty", 'education_level' ]

    def get_photo(self, object):
        if object.preview:
            return mark_safe(f"<img src='{object.preview.url}' height=80>")

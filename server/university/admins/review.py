from django.contrib import admin
from django.utils.safestring import mark_safe

from university.models.review import StudentReview, StudentSpeak


@admin.register(StudentReview)
class StudentReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_photo']
    readonly_fields = ["get_photo"]
    search_fields = ["name"]
    filter_horizontal = [ "faculty", 'education_level' ]

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=80>")


@admin.register(StudentSpeak)
class StudentSpeakAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_photo']
    readonly_fields = ["get_photo"]
    search_fields = ["name"]
    filter_horizontal = [ "faculty", 'education_level' ]

    def get_photo(self, object):
        if object.preview:
            return mark_safe(f"<img src='{object.preview.url}' height=80>")

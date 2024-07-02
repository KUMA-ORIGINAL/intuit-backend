from django.contrib import admin
from django.utils.safestring import mark_safe

from university.models.education_level import EducationLevel, AdmissionEligibility


@admin.register(AdmissionEligibility)
class AdmissionEligibilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "get_photo"]
    search_fields = ["title"]
    list_filter = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    list_per_page = 20
    readonly_fields = ["get_photo"]

    def get_photo(self, object):
        if object.banner:
            return mark_safe(f"<img src='{object.banner.url}' height=80>")
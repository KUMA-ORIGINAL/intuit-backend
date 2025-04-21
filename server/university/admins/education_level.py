from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

from university.models.education_level import EducationLevel, AdmissionEligibility


@admin.register(AdmissionEligibility)
class AdmissionEligibilityAdmin(TranslationAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(EducationLevel)
class EducationLevelAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title', 'get_icon', "get_banner"]
    list_display_links = ['id', 'title']
    search_fields = ["title"]
    list_filter = ["title"]
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
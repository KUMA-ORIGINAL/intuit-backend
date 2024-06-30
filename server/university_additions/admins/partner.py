from django.contrib import admin
from django.utils.safestring import mark_safe

from university_additions.models.partner import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_logo']
    readonly_fields = ["get_logo"]
    search_fields = ["title"]
    filter_horizontal = ["faculty"]

    def get_logo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' height=100>")

    get_logo.short_description = "логотип"

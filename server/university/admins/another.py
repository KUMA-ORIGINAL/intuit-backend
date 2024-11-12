from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from university.models import Detail


@admin.register(Detail)
class DetailAdmin(TranslationAdmin):
    list_display = ["id", "title", 'subtitle']
    list_display_links = ["id"]
    search_fields = ["title", "subtitle"]
    list_per_page = 20

from django.contrib import admin

from university.models import Detail


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ["id", "title", 'subtitle']
    list_display_links = ["id"]
    search_fields = ["title", "subtitle"]
    list_per_page = 20

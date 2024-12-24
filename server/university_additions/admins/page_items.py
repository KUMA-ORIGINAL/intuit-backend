from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from ..models import PageItem, PageItems

class PageItemsInline(TranslationTabularInline):  # Inline для изображений
    model = PageItems
    extra = 1  # Количество пустых форм для добавления новых изображений

@admin.register(PageItem)
class PageItemAdmin(TabbedTranslationAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ["title"]}
    inlines = [PageItemsInline] # Добавляем Inline для изображений

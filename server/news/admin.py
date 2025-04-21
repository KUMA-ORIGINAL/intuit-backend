from django.contrib import admin
from django.db import models

from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

from common.admin import AutoTranslateAdmin
from .models import Post, Image, File, Category, Event


@admin.register(Post)
class PostAdmin(AutoTranslateAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": CKEditorWidget,
        }
    }
    list_display = ["title", "status", "date"]
    list_filter = ['date', 'status', 'categories']
    ordering = ['-date', 'status',]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description']
    date_hierarchy = 'date'
    list_editable = ['status']
    save_on_top = True
    list_per_page = 20
    save_as = True


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['id', "title"]
    list_display_links = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Image)
class ImageAdmin(TranslationAdmin):
    list_display = ["title", 'image', 'photo']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 20

    def photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=100>")


@admin.register(File)
class FileAdmin(TranslationAdmin):
    list_display = ["title", "file"]


@admin.register(Event)
class EventAdmin(TabbedTranslationAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": CKEditorWidget,
        }
    }
    list_display = ["title", "status", "created_at"]
    list_filter = ['created_at', 'status',]
    ordering = ['-created_at', 'status',]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description']
    filter_horizontal = [ 'faculty']
    list_editable = ['status']
    save_on_top = True
    list_per_page = 20
    readonly_fields = ['created_at',]

    fieldsets = (
        ("Пост", {
            'fields': ('title', 'slug', "description",)
        }),
        ("Дополнительно", {
            'fields': ("banner",)
        }),
        ("Параметры", {
            'fields': ('status', "created_at", 'faculty')
        }),

    )
    save_as = True

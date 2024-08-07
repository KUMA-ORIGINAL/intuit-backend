from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe

from .models import Post, Image, File, Category


class PostForm(forms.ModelForm):
    description = forms.CharField(empty_value='', widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ["title", "status", "date"]
    list_filter = ['date', 'status', 'categories']
    ordering = ['-status', '-date']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description']
    filter_horizontal = ['categories', 'files', 'images']
    date_hierarchy = 'date'
    list_editable = ['status']
    save_on_top = True
    fieldsets = (
        ("Пост", {
            'fields': ('title', "description",)
        }),
        ("Дополнительно", {
            'fields': ("banner", "images", "files")
        }),
        ("Параметры", {
            'fields': ('status', "slug", "date", "categories")
        }),

    )
    save_as = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", 'image', 'photo']
    list_filter = ['title']
    search_fields = ['title']

    def photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=100>")


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ["title", "file"]

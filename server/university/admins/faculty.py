from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedTranslationAdmin

from university.models.faculty import Faculty

class FacultyForm(forms.ModelForm):
    text_ru = forms.CharField(empty_value='', widget=CKEditorWidget())
    text_en = forms.CharField(required=False, empty_value='', widget=CKEditorWidget())
    text_ky = forms.CharField(required=False, empty_value='', widget=CKEditorWidget())
    subtext_ru = forms.CharField(empty_value='', widget=CKEditorWidget())
    subtext_en = forms.CharField(required=False, empty_value='', widget=CKEditorWidget())
    subtext_ky = forms.CharField(required=False, empty_value='', widget=CKEditorWidget())

    class Meta:
        model = Faculty
        fields = '__all__'


@admin.register(Faculty)
class FacultyAdmin(TabbedTranslationAdmin):
    form = FacultyForm
    list_display = ['id', 'title', "get_photo"]
    list_display_links = ['id', 'title',]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    list_per_page = 20
    readonly_fields = ["get_photo"]

    def get_photo(self, object):
        if object.banner:
            return mark_safe(f"<img src='{object.banner.url}' height=80>")

from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedTranslationAdmin

from document_pages.models import DocumentPage


class DocumentPageForm(forms.ModelForm):
    content_ru = forms.CharField(empty_value='', widget=CKEditorWidget())
    content_en = forms.CharField(required=False, empty_value='', widget=CKEditorWidget())
    content_ky = forms.CharField(required=False, empty_value='', widget=CKEditorWidget())

    class Meta:
        model = DocumentPage
        fields = '__all__'


@admin.register(DocumentPage)
class DocumentPageAdmin(TabbedTranslationAdmin):
    form = DocumentPageForm
    list_display = ('title', 'subtitle', 'photo_preview')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('document_collections',)

    def photo_preview(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=150>")

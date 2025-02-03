from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from ..models import DocumentCollection, DocumentCollectionItem


class DocumentCollectionItemInline(TranslationTabularInline):
    model = DocumentCollectionItem
    extra = 1


@admin.register(DocumentCollection)
class DocumentCollectionAdmin(TabbedTranslationAdmin):
    list_display = ('name',)
    inlines = (DocumentCollectionItemInline,)

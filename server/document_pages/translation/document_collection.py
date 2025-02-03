from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import DocumentCollection


@register(DocumentCollection)
class DocumentCollectionTranslationOptions(TranslationOptions):
    fields = ('name',)

from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import DocumentCollectionItem


@register(DocumentCollectionItem)
class DocumentCollectionItemTranslationOptions(TranslationOptions):
    fields = ('name', 'document')

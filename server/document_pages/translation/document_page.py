from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import DocumentPage


@register(DocumentPage)
class DocumentPageTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')

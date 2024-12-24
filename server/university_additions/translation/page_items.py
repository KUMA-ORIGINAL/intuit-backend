from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import PageItem, PageItems


@register(PageItem)
class PageItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(PageItems)
class PageItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


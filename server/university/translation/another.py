from modeltranslation.translator import register, TranslationOptions
from ..models import Detail


@register(Detail)
class DetailTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')

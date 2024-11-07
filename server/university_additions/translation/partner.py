from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import Partner

@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title',)

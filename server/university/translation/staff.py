from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import Staff, Position


@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ('name', 'rank',  'status', 'description', 'cv')

@register(Position)
class PositionTranslationOptions(TranslationOptions):
    fields = ('title', )

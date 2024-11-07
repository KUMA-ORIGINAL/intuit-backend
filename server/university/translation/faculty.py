from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import Faculty


@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'text','subtext')

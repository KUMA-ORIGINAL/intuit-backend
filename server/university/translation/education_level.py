from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import AdmissionEligibility, EducationLevel

@register(AdmissionEligibility)
class AdmissionEligibilityTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(EducationLevel)
class EducationLevelTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'text','subtext',
              'study_period', 'employment', 'diploma')

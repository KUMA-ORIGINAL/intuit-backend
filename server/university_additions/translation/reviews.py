from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from university_additions.models import StudentReview, StudentSpeak


@register(StudentReview)
class StudentReviewTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(StudentSpeak)
class StudentSpeakTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

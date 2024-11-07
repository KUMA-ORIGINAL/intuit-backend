from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import Program, TrainingProgramItem, ProgramSkills, ProgramTools, ProgramProfessions


@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'subtext',
              'study_period', 'training_form',
              'employment', 'diploma')

@register(TrainingProgramItem)
class TrainingProgramItemTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ProgramSkills)
class ProgramSkillsTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ProgramTools)
class ProgramToolsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(ProgramProfessions)
class ProgramProfessionsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

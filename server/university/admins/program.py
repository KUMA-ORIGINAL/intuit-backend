from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, \
    TabbedTranslationAdmin

from university.models.program import Program, TrainingProgram, TrainingProgramItem, ProgramSkills, \
    ProgramTools, ProgramProfessions


class TrainingProgramItemInline(TranslationTabularInline):
    model = TrainingProgramItem
    extra = 1


class ProgramSkillsInline(admin.TabularInline):
    model = ProgramSkills.program.through
    extra = 1
    verbose_name = 'Навык который изучишь в программе'
    verbose_name_plural = 'Навыки которые изучишь в программе'


class ProgramToolsInline(admin.TabularInline):
    model = ProgramTools.program.through
    extra = 1
    verbose_name = 'Инструмент который изучишь в программе'
    verbose_name_plural = 'Инструменты которые изучишь в программе'


class ProgramProfessionsInline(admin.TabularInline):
    model = ProgramProfessions.program.through
    extra = 1
    verbose_name = 'Профессию которую освоишь в программе'
    verbose_name_plural = 'Профессии которую освоишь в программе'




class ProgramForm(forms.ModelForm):
    subtext_ru = forms.CharField(empty_value='', widget=CKEditorWidget())
    subtext_en = forms.CharField(required=False, empty_value='', widget=CKEditorWidget())
    subtext_ky = forms.CharField(required=False, empty_value='', widget=CKEditorWidget())

    class Meta:
        model = Program
        fields = '__all__'


@admin.register(Program)
class ProgramAdmin(TabbedTranslationAdmin):
    form = ProgramForm
    list_display = ['id', 'title', 'get_photo']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['title']
    prepopulated_fields = {'slug': ['title']}
    list_per_page = 20
    readonly_fields = ['get_photo']
    filter_horizontal = ['faculty', 'education_level']
    inlines = [ProgramSkillsInline, ProgramToolsInline, ProgramProfessionsInline]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' height=100>")
        return ''
    get_photo.short_description = 'Фото'



@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    inlines = [TrainingProgramItemInline]
    list_display = ['number', 'program']
    list_filter = ['program']
    search_fields = ['number']


@admin.register(ProgramSkills)
class ProgramSkillsAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'name', 'get_programs']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    filter_horizontal = ('program',)

    def get_programs(self, obj):
        return ", ".join([p.title for p in obj.program.all()])
    get_programs.short_description = 'Программы'



@admin.register(ProgramTools)
class ProgramToolsAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'name', 'get_logo', 'get_programs']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    filter_horizontal = ('program',)

    def get_programs(self, obj):
        return ", ".join([p.title for p in obj.program.all()])
    get_programs.short_description = 'Программы'

    def get_logo(self, obj):
        if obj.logo:
            return mark_safe(f"<img src='{obj.logo.url}' height=80>")
        return ''
    get_logo.short_description = 'Лого инструмента'


@admin.register(ProgramProfessions)
class ProgramProfessionsAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'name', 'get_photo', 'get_programs']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    filter_horizontal = ('program',)

    def get_programs(self, obj):
        return ", ".join([p.title for p in obj.program.all()])
    get_programs.short_description = 'Программы'

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' height=80>")
        return ''
    get_photo.short_description = 'Фото профессии'

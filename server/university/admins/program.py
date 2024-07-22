from django.contrib import admin
from django.utils.safestring import mark_safe

from university.models.program import Program, TrainingProgram, TrainingProgramItem, ProgramSkills, \
    ProgramTools, ProgramProfessions


class TrainingProgramItemInline(admin.TabularInline):
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


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_photo']
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
class ProgramSkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_programs']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    filter_horizontal = ('program',)

    def get_programs(self, obj):
        return ", ".join([p.title for p in obj.program.all()])
    get_programs.short_description = 'Программы'

@admin.register(ProgramTools)
class ProgramToolsAdmin(admin.ModelAdmin):
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
class ProgramProfessionsAdmin(admin.ModelAdmin):
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

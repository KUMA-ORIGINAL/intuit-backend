from ckeditor.fields import RichTextField
from django.db import models


class Program(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="ссылка")
    photo = models.FileField(verbose_name="Фото", upload_to='programs')
    text = models.CharField(verbose_name="Заголовок", max_length=250,
                                blank=True)
    subtext = RichTextField(verbose_name="Описание", default="Описание")
    text_photo = models.FileField(verbose_name="Фото", upload_to='programs')

    study_period = models.CharField(verbose_name="Срок обучения", max_length=255)
    training_form = models.CharField(verbose_name="Форма обучения", max_length=255)
    employment = models.CharField(verbose_name="Трудоустройство", max_length=255)
    diploma = models.CharField(verbose_name="Диплом", max_length=255)

    education_level = models.ManyToManyField('EducationLevel',
                                        verbose_name="Уровень образования",)
    faculty = models.ManyToManyField('Faculty',
                                verbose_name="Факультет")

    # detail = models.ManyToManyField(to="Detail",
    #                                 verbose_name="Детали")

    class Meta:
        ordering = ("title",)
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

    def __str__(self):
        return self.title


class TrainingProgram(models.Model):
    number = models.IntegerField(verbose_name='Номер курса')
    program = models.ForeignKey(Program, related_name='training_programs',
                                on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = "Программа обучения"
        verbose_name_plural = "Программы обучения"

    def __str__(self):
        return f"{self.number} курс в программе {self.program}"


class TrainingProgramItem(models.Model):
    training_program = models.ForeignKey(TrainingProgram, related_name='items',
                                        on_delete=models.CASCADE)
    name = models.TextField(verbose_name='Навык')

    class Meta:
        verbose_name = "Элемент программы обучения"
        verbose_name_plural = "Элементы программы обучения"

    def __str__(self):
        return self.name


class ProgramSkills(models.Model):
    name = models.CharField(verbose_name='Навык', max_length=255)
    program = models.ManyToManyField(Program,
                                     verbose_name="Программа",
                                     related_name="skills",
                                     blank=True)

    class Meta:
        verbose_name = "Навык программы"
        verbose_name_plural = "Навыки программы"

    def __str__(self):
        return self.name


class ProgramTools(models.Model):
    name = models.CharField(verbose_name='Инструмент', max_length=255)
    logo = models.FileField(verbose_name='Лого инструмента', upload_to='programs/program-tools/')
    program = models.ManyToManyField(Program,
                                     verbose_name="Программа",
                                     related_name="tools",
                                     blank=True)

    class Meta:
        verbose_name = "Инструмент программы"
        verbose_name_plural = "Инструменты программы"

    def __str__(self):
        return self.name


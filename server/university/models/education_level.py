from ckeditor.fields import RichTextField
from django.db import models

class AdmissionEligibility(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)

    class Meta:
        ordering = ("name",)
        verbose_name = "Допуск к поступлению"
        verbose_name_plural = "Допуск к поступлениям"

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(verbose_name="ссылка")
    subtitle = models.CharField(verbose_name="Под название", max_length=255,
                                blank=True)
    banner = models.FileField(verbose_name="баннер", upload_to='education-levels')

    text = models.TextField(verbose_name="Главный текст")
    subtext = models.TextField(verbose_name="Под текст")

    program_count = models.PositiveIntegerField(verbose_name="Количество программ",
                                                default=0,
                                                blank=True)
    study_period = models.CharField(verbose_name="Срок обучения", max_length=255)
    employment = models.CharField(verbose_name="Трудоустройство", max_length=255)
    diploma = models.CharField(verbose_name="Диплом", max_length=255)

    admission_eligibility = models.ManyToManyField(AdmissionEligibility,
                                                   verbose_name="Подходимость для поступления")

    # detail = models.ManyToManyField("Detail",
    #                                 verbose_name="Детали")

    class Meta:
        ordering = ("title",)
        verbose_name = "Уровень образования"
        verbose_name_plural = "Уровни образования"

    def __str__(self):
        return self.title

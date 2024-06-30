from ckeditor.fields import RichTextField
from django.db import models


class Program(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="ссылка")
    subtitle = models.CharField(verbose_name="Заголовок", max_length=250,
                                blank=True)
    description = RichTextField(verbose_name="Описание", default="Описание")
    photo = models.ImageField(verbose_name="Фото", upload_to='programs')

    education_level = models.ForeignKey('EducationLevel',
                                        verbose_name="Уровень образования",
                                        on_delete=models.CASCADE)
    faculty = models.ForeignKey('Faculty',
                                verbose_name="Факультет",
                                on_delete=models.CASCADE)
    detail = models.ManyToManyField(to="Detail",
                                    verbose_name="Детали")

    class Meta:
        ordering = ("title",)
        verbose_name = "Программа обучения"
        verbose_name_plural = "Программы обучения"

    def __str__(self):
        return self.title

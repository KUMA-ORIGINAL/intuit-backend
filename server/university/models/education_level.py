from ckeditor.fields import RichTextField
from django.db import models


class EducationLevel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(verbose_name="ссылка")
    subtitle = models.CharField(verbose_name="Заголовок", max_length=255,
                                blank=True)
    photo = models.ImageField(verbose_name="Фото", upload_to='education-levels')

    title_2 = models.CharField(verbose_name="Название", max_length=255)
    description = RichTextField(verbose_name="Описание", default="Описание")

    detail = models.ManyToManyField("Detail",
                                    verbose_name="Детали")

    class Meta:
        ordering = ("title",)
        verbose_name = "Уровень образования"
        verbose_name_plural = "Уровни образования"

    def __str__(self):
        return self.title

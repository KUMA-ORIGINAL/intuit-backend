from django.db import models


class Faculty(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(verbose_name="ссылка")
    subtitle = models.CharField(verbose_name="Заголовок", max_length=255,
                                blank=True)
    photo = models.ImageField(verbose_name="Фото", upload_to='faculty')

    education_level = models.ForeignKey('EducationLevel',
                                        verbose_name="Уровень образования",
                                        on_delete=models.CASCADE)
    detail = models.ManyToManyField(to="Detail",
                                    verbose_name="Детали")

    class Meta:
        ordering = ("title",)
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    def __str__(self):
        return self.title

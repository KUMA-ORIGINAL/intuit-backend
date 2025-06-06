from django.db import models


class Faculty(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(verbose_name="ссылка")
    icon = models.FileField(verbose_name='Иконка', upload_to='faculties-icons', null=True, blank=True)
    banner = models.FileField(verbose_name="Баннер", upload_to='faculties')

    subtitle = models.CharField(verbose_name="Заголовок", max_length=250,
                                blank=True)

    text = models.TextField(verbose_name="Главный текст")
    subtext = models.TextField(verbose_name="Под текст")

    education_level = models.ManyToManyField('EducationLevel',
                                        verbose_name="Уровень образования")

    program_count = models.PositiveIntegerField(verbose_name="Количество программ",
                                                default=0,
                                                blank=True)
    document_collections = models.ManyToManyField('document_pages.DocumentCollection',
                                                  verbose_name='Коллекции документов',
                                                  blank=True,)
    # detail = models.ManyToManyField(to="Detail",
    #                                 verbose_name="Детали")

    class Meta:
        ordering = ("title",)
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    def __str__(self):
        return self.title

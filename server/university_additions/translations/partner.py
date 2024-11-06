from django.db import models

from university.models import Faculty


class Partner(models.Model):
    title = models.CharField(verbose_name="Название", max_length=200)
    logo = models.FileField(verbose_name="Логотип", upload_to="partners/logo/")
    faculty = models.ManyToManyField(Faculty,
                                     verbose_name="Институты",
                                     related_name="partners",
                                     blank=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.title

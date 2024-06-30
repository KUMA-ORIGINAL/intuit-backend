from django.db import models


class Detail(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=500)
    subtitle = models.CharField(verbose_name="Подзаголовок", max_length=250, blank=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"

    def __str__(self):
        return f"{self.title} / {self.subtitle}"

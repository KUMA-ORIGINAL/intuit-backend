from django.db import models


class PageItem(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name="ссылка")
    cover = models.FileField(verbose_name="Фото", upload_to="page-item/")
    description = models.TextField(blank=True, null=True)  # Описание страницы

    def __str__(self):
        return self.title


# Модель для сущностей, которые могут повторяться (например, студенты, колледжи)
class PageItems(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cover = models.FileField(verbose_name="Фото", upload_to="page-item/page-items/")
    link = models.URLField(blank=True, null=True)  # Внешняя ссылка
    is_external = models.BooleanField(default=False)  # Является ли ссылка внешней
    page_item = models.ForeignKey(PageItem, on_delete=models.CASCADE,
                                  related_name='items')  # Связь ForeignKey

    def __str__(self):
        return self.title

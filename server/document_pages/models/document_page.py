from django.db import models


class DocumentPage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=255, verbose_name='Под заголовок')
    photo = models.FileField(verbose_name="Фото", upload_to="document_pages/photos/%Y/%m/")
    content = models.TextField(verbose_name='Контент')
    document_collections = models.ManyToManyField('DocumentCollection',
                                                  verbose_name='Коллекции документов')

    class Meta:
        verbose_name = "Страница документов"
        verbose_name_plural = "Страницы документов"

    def __str__(self):
        return self.title

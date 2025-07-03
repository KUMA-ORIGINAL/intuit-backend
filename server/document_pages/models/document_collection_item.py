from django.db import models


class DocumentCollectionItem(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название файла')
    document = models.FileField(upload_to='document_pages/files/%Y/%m/', verbose_name='Файл')
    document_collection = models.ForeignKey('DocumentCollection',
                                            on_delete=models.CASCADE,
                                            related_name='document_collection_items')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок', blank=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['order']

    def __str__(self):
        return self.name

from django.db import models


class DocumentCollection(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название коллекции')

    class Meta:
        verbose_name = "Коллекция документов"
        verbose_name_plural = "Коллекции документов"

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ("active", "активен"),
        ("passive", "не активен")
    )

    status = models.CharField(verbose_name="Статус", choices=STATUS_CHOICES, max_length=15, default="passive")

    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка", unique_for_date='date')
    description = models.TextField(verbose_name="Текст")

    date = models.DateTimeField(verbose_name="Дата", default=timezone.now)

    banner = models.FileField(verbose_name="Баннер", upload_to="news/banners/%Y/%m/%d")
    categories = models.ManyToManyField('Category', related_name='posts', verbose_name='Категории')
    faculty = models.ManyToManyField('university.Faculty', related_name='posts',
                                     verbose_name='Категории2')
    images = models.ManyToManyField('Image', related_name='posts', verbose_name='Фотографии',
                                    blank=True)
    files = models.ManyToManyField('File', related_name='posts', verbose_name='Файлы', blank=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка")

    class Meta:
        ordering = ('title',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    image = models.FileField(verbose_name="Изображение", upload_to="news/images/posts/%Y/%m/%d", blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    file = models.FileField(verbose_name="Файл", upload_to="news/files/posts/%Y/%m/%d", blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.title

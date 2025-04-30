from django.db import models

from university.models import Faculty, EducationLevel


class StudentReview(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=250)
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(verbose_name='Фото', upload_to='students/reviews')
    faculty = models.ManyToManyField(verbose_name="Институты",
                                     to=Faculty,
                                     related_name="student_reviews",
                                     blank=True)
    education_level = models.ManyToManyField(verbose_name='Уровни образования',
                                             to=EducationLevel,
                                             blank=True)

    class Meta:
        verbose_name = 'Отзыв студента'
        verbose_name_plural = 'Отзывы студентов'

    def __str__(self):
        return self.name


class StudentSpeak(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=255)
    preview = models.ImageField(verbose_name='Фото', upload_to='students/reviews-preview',
                                help_text='Фото для предварительного просмотра')
    video_url = models.URLField(verbose_name="Ссылка на видео", max_length=255)
    faculty = models.ManyToManyField(verbose_name="Институты",
                                     to=Faculty,
                                     related_name="student_speakers",
                                     blank=True)
    education_level = models.ManyToManyField(verbose_name='Уровни образования',
                                             to=EducationLevel,
                                             blank=True)

    class Meta:
        verbose_name = 'Говор студента'
        verbose_name_plural = 'Говоры студентов'

    def __str__(self):
        return self.name

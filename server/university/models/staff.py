from django.db import models


class Staff(models.Model):
    STATUS_CHOISE = (
        ("1", "Преподаватель"),
        ("2", "Старший преподаватель"),
        ("3", "Кандитат наук"),
        ("4", "Профессор"),
        ("5", "Доцент")
    )
    RANK_CHOISE = (
        ("no", "Отсутствует"),
        ("professor", "Почетный профессор"),
        ("doctor", "Почетный доктор"),
    )

    name = models.CharField(verbose_name="ФИО", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка", blank=True)
    position = models.ForeignKey(verbose_name="Должность", to="Position",
                                 on_delete=models.CASCADE, default=2, related_name='teachers')
    faculty = models.ManyToManyField(to='Faculty',
                                     verbose_name="Факультеты",
                                     related_name='teachers', null=True, blank=True)
    rank = models.CharField(verbose_name="Статус", max_length=50,
                            choices=RANK_CHOISE, default="no")

    status = models.CharField(verbose_name="Звание", choices=STATUS_CHOISE, default="1",
                              max_length=20)

    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.FileField(verbose_name="Изображение", upload_to="faculty/images/teachers")

    facebook = models.CharField(
        verbose_name="facebook",
        help_text='Введите ссылку на профиль (не обязательное полое)',
        max_length=100,
        blank=True)

    telegram = models.CharField(
        verbose_name="Телеграм",
        help_text="Введите ссылку на профиль (не обязательное полое)",
        max_length=100,
        blank=True)

    instagram = models.CharField(
        verbose_name="Инстаграм",
        help_text="Введите ссылку на профиль (не обязательное полое)",
        max_length=100,
        blank=True)

    youtube = models.CharField(
        verbose_name="YouTube",
        help_text="Введите ссылку на профиль (не обязательное полое)",
        max_length=100,
        blank=True)

    curriculum_vitae = models.FileField(
        verbose_name="Сurriculum Vitae",
        upload_to="faculty/files/cv",
        blank=True)

    cv = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("position",)
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(verbose_name="Должность", max_length=100)
    level = models.IntegerField(verbose_name="Приоритет должности")

    class Meta:
        ordering = ['level']
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.title

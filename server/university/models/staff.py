import os
from io import BytesIO

import qrcode
from django.core.files import File
from django.db import models
from django.utils.text import slugify

from server import settings


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

    whatsapp = models.CharField(
        verbose_name="whatsApp",
        help_text='Введите ссылку на профиль (не обязательное полое)',
        max_length=100,
        blank=True)

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

    qr_code = models.ImageField(upload_to='faculty/qr_codes/', blank=True)

    class Meta:
        ordering = ("position",)
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.name

    def delete_old_qr_code(self):
        if self.qr_code:
            if os.path.isfile(self.qr_code.path):
                os.remove(self.qr_code.path)

    def generate_qr_code(self):
        link = f"{settings.SITE_URL}/teachers/{self.slug}/"  # Ссылка на страницу преподавателя
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        # Сохраняем изображение в памяти
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Сохраняем файл QR-кода
        file_name = f'qr_code_{self.slug}.png'
        self.qr_code.save(file_name, File(buffer), save=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        # Проверяем, изменился ли slug или отсутствует qr_code
        should_generate_qr = False
        if not self.qr_code or self.pk is None:
            should_generate_qr = True
        else:
            old_instance = Staff.objects.filter(pk=self.pk).first()
            if old_instance and old_instance.slug != self.slug:
                should_generate_qr = True

        # Удаляем старый QR-код, если требуется его пересоздать
        if should_generate_qr and self.qr_code:
            self.delete_old_qr_code()

        # Генерация QR-кода, если требуется
        if should_generate_qr:
            self.generate_qr_code()

        super().save(*args, **kwargs)


class Position(models.Model):
    title = models.CharField(verbose_name="Должность", max_length=100)
    level = models.IntegerField(verbose_name="Приоритет должности")

    class Meta:
        ordering = ['level']
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.title

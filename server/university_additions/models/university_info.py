from django.db import models


class UniversityInfo(models.Model):
    address = models.CharField(verbose_name="Адрес", max_length=255)
    hours_weekdays = models.CharField(verbose_name="Часы работы в будни",max_length=50)
    hours_saturday = models.CharField(verbose_name="Часы работы в субботу", max_length=50)
    hours_sunday = models.CharField(verbose_name="Часы работы в воскресенье", max_length=50)
    reception_phone = models.CharField(verbose_name="Телефон для общих вопросов", max_length=20)
    admission_office_phone = models.CharField(verbose_name="Телефон приёмной комиссии",
                                              max_length=20)

    whatsapp = models.CharField(
        verbose_name="whatsApp",
        help_text='Введите ссылку на профиль (не обязательное полое)',
        max_length=100,
        blank=True)

    facebook = models.CharField(
        verbose_name="Facebook",
        help_text='Введите ссылку на профиль (не обязательное полое)',
        max_length=100,
        blank=True)

    telegram = models.CharField(
        verbose_name="Telegram",
        help_text="Введите ссылку на профиль (не обязательное полое)",
        max_length=100,
        blank=True)

    instagram = models.CharField(
        verbose_name="Instagram",
        help_text="Введите ссылку на профиль (не обязательное полое)",
        max_length=100,
        blank=True)

    youtube = models.CharField(
        verbose_name="YouTube",
        help_text="Введите ссылку на профиль (не обязательное полое)",
        max_length=100,
        blank=True)

    class Meta:
        verbose_name = "Информация об университете"
        verbose_name_plural = "Информация об университете"

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(id=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        super(UniversityInfo, self).save(*args, **kwargs)
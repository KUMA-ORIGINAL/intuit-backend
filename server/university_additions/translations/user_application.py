from django.db import models


class UserApplication(models.Model):
    STATUS_CHOICES = (
        ("active", "активный"),
        ("passive", "не активный")
    )

    user = models.CharField(verbose_name="Имя", max_length=250)
    phone = models.CharField(verbose_name="Телефон", max_length=50)
    email = models.EmailField(verbose_name="email", max_length=50, default="")
    slug = models.CharField(verbose_name="путь к странице сайте")
    status = models.CharField(verbose_name="Статус", choices=STATUS_CHOICES, max_length=15,
                              default="active")
    created = models.DateTimeField(verbose_name="Дата регистрации", auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name = "Заявка пользователя"
        verbose_name_plural = "Заявки пользователей"

    def __str__(self):
        return self.user

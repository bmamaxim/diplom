from django.contrib.auth.models import AbstractUser
from django.db import models

from service.models import NULLABLE


class User(AbstractUser):
    username = None
    first_name = models.ImageField(
        max_length=50, verbose_name="Имя", help_text="Введите ваше имя", **NULLABLE
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию",
        **NULLABLE,
    )
    tg_id = models.CharField(max_length=200, verbose_name="Телеграмм", **NULLABLE)
    email = models.EmailField(
        unique=True,
        verbose_name="Элктронная почта",
        help_text="Введите адрес электронной почты",
    )
    ver_code = models.CharField(
        max_length=4, verbose_name="Код верификации", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

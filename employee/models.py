from django.db import models

from service.models import NULLABLE


class Employee(models.Model):
    """
    Модель сотрудника клиники.
    """

    name = models.CharField(
        max_length=300,
        help_text="Введите название направления",
        verbose_name="название",
    )
    room = models.IntegerField(help_text="Укажите номер кабинета", verbose_name="кабинет"
    )
    first_name = models.CharField(
        max_length=100, help_text="Имя врача", verbose_name="имя", **NULLABLE
    )
    last_name = models.CharField(
        max_length=100, help_text="Фамилия врача", verbose_name="Фамилмя", **NULLABLE
    )
    image = models.ImageField(
        upload_to="image/", verbose_name="изображение", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}" f"{self.room}" f"{self.first_name}" f"{self.last_name}"

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

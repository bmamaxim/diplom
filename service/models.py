import datetime

from django.db import models

from config import settings
from employee.models import Employee, NULLABLE


class Service(models.Model):
    """
    Модель предоставляемых услуг.
    """

    name = models.CharField(
        max_length=300,
        help_text="Введите название услуги",
        verbose_name="Название услуги",
    )
    description = models.CharField(
        max_length=500,
        help_text="Опишите услугу",
        verbose_name="Описание услуги",
        **NULLABLE,
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        help_text="Выберите сотрудника",
        verbose_name="Сотрудник",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}" f"{self.description}"

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"


class SignUp(models.Model):
    """
    Модель записи.
    """

    time_list = [
        datetime.time(hour=8).strftime("%H:%m:%S"),
        datetime.time(hour=9).strftime("%H:%m:%S"),
        datetime.time(hour=10).strftime("%H:%m:%S"),
        datetime.time(hour=11).strftime("%H:%m:%S"),
        datetime.time(hour=13).strftime("%H:%m:%S"),
        datetime.time(hour=14).strftime("%H:%m:%S"),
        datetime.time(hour=15).strftime("%H:%m:%S"),
        datetime.time(hour=16).strftime("%H:%m:%S"),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        help_text="Выбыерите сотрудника",
        verbose_name="Сотрудник",
        **NULLABLE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пациент",
        **NULLABLE,
    )
    time = models.TimeField(
        help_text="Выберите время записи",
        verbose_name="время записи",
        **NULLABLE,
    )
    date = models.DateField(
        verbose_name="Дата записи",
        help_text="Выберите дату записи",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.time} {self.date}"

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"

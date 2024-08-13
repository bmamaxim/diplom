from datetime import datetime, timedelta

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

    datetime_now = datetime.today().date()

    TODAY = datetime_now
    TOMORROW = datetime_now + timedelta(days=1)
    DAY_AFTER_TOMORROW = datetime_now + timedelta(days=2)

    DATE = (
        (TODAY, TODAY),
        (TOMORROW, TOMORROW),
        (DAY_AFTER_TOMORROW, DAY_AFTER_TOMORROW),
    )

    EIGHT = "08:00"
    NINE = "09:00"
    TEN = "10:00"
    ELEVEN = "11:00"
    THIRTEEN = "13:00"
    FOURTEEN = "14:00"
    FIFTEEN = "15:00"
    SIXTEEN = "16:00"

    TIME = (
        (EIGHT, "08:00"),
        (NINE, "09:00"),
        (TEN, "10:00"),
        (ELEVEN, "11:00"),
        (THIRTEEN, "13:00"),
        (FOURTEEN, "14:00"),
        (FIFTEEN, "15:00"),
        (SIXTEEN, "16:00"),
    )

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
    time = models.CharField(
        choices=TIME, help_text="Выберите время записи", verbose_name="время записи"
    )
    date = models.DateField(
        choices=DATE, verbose_name="Дата записи", help_text="Выберите дату записи"
    )

    def __str__(self):
        return f"{self.time} {self.date}"

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"

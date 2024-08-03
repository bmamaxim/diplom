from django.db import models

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
    Модель записи
    """
    pass

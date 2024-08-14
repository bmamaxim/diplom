from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Employee(models.Model):
    """
    Модель сотрудника клиники.
    """

    THERAPIST = "Therapist"
    OPHTHALMOLOGIST = "Ophthalmologist"
    NURSE = "nurse"

    DOCTOR = (
        (THERAPIST, "Терапевт"),
        (OPHTHALMOLOGIST, "Офтальмолог"),
        (NURSE, "Медсестра"),
    )

    name = models.CharField(
        choices=DOCTOR,
        default=None,
        help_text="Выберите название направления",
        verbose_name="Название",
    )
    room = models.IntegerField(
        help_text="Укажите номер кабинета", verbose_name="Кабинет"
    )
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, **NULLABLE
    )
    photo = models.ImageField(
        upload_to="image/", verbose_name="изображение", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}" f"{self.room}" f"{self.employee}"

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

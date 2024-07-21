from django.db import models

NULLABLE = {"blank": True, "null": True}


class Service(models.Model):
    name = models.CharField(
        max_length=300,
        help_text="Введите название услугу",
        verbose_name="Название услуги",
    )
    description = models.CharField(
        max_length=500,
        help_text="Опишите услугу",
        verbose_name="Описание услуги",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}" f"{self.description}"

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

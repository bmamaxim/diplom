# Generated by Django 4.2 on 2024-08-03 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0005_employee_photo"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("service", "0002_service_employee_alter_service_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="SignUp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.CharField(
                        choices=[
                            (8, 8),
                            (9, 9),
                            (10, 10),
                            (11, 11),
                            (13, 13),
                            (14, 14),
                            (15, 15),
                            (16, 16),
                        ],
                        help_text="Выберите время записи",
                        verbose_name="время записи",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        help_text="Выберите дату записи", verbose_name="Дата записи"
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        help_text="Выбыерите сотрудника",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.employee",
                        verbose_name="Сотрудник",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пациент",
                    ),
                ),
            ],
        ),
    ]
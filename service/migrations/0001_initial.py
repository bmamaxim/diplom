# Generated by Django 4.2 on 2024-07-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                    "name",
                    models.CharField(
                        help_text="Введите название услугу",
                        max_length=300,
                        verbose_name="Название услуги",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="Опишите услугу",
                        max_length=500,
                        null=True,
                        verbose_name="Описание услуги",
                    ),
                ),
            ],
            options={
                "verbose_name": "услуга",
                "verbose_name_plural": "услуги",
            },
        ),
    ]

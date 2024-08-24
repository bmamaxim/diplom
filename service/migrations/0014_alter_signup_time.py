# Generated by Django 4.2 on 2024-08-14 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0013_alter_signup_date_alter_signup_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup",
            name="time",
            field=models.CharField(
                choices=[
                    (
                        datetime.timedelta(seconds=28800),
                        datetime.timedelta(seconds=28800),
                    ),
                    (
                        datetime.timedelta(seconds=32400),
                        datetime.timedelta(seconds=32400),
                    ),
                    (
                        datetime.timedelta(seconds=36000),
                        datetime.timedelta(seconds=36000),
                    ),
                    (
                        datetime.timedelta(seconds=39600),
                        datetime.timedelta(seconds=39600),
                    ),
                    (
                        datetime.timedelta(seconds=46800),
                        datetime.timedelta(seconds=46800),
                    ),
                    (
                        datetime.timedelta(seconds=50400),
                        datetime.timedelta(seconds=50400),
                    ),
                    (
                        datetime.timedelta(seconds=54000),
                        datetime.timedelta(seconds=54000),
                    ),
                    (
                        datetime.timedelta(seconds=57600),
                        datetime.timedelta(seconds=57600),
                    ),
                ],
                help_text="Выберите время записи",
                verbose_name="время записи",
            ),
        ),
    ]
# Generated by Django 4.2 on 2024-07-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="password",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="password"
            ),
        ),
    ]
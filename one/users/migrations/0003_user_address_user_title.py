# Generated by Django 4.2.8 on 2024-01-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(blank=True, max_length=255, verbose_name="Address"),
        ),
        migrations.AddField(
            model_name="user",
            name="title",
            field=models.CharField(blank=True, max_length=255, verbose_name="Title"),
        ),
    ]

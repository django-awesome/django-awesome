# Generated by Django 4.2.8 on 2024-01-22 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogDetail",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uid", models.CharField(blank=True, max_length=50, null=True, verbose_name="UID")),
                ("metadata", models.JSONField(blank=True, default=dict, null=True, verbose_name="Meta")),
                ("snapshot", models.JSONField(blank=True, default=dict, null=True, verbose_name="Snapshot")),
                (
                    "diffs",
                    models.JSONField(
                        blank=True, default=list, null=True, verbose_name="Different with previous version"
                    ),
                ),
                (
                    "logentry",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="detail", to="admin.logentry"
                    ),
                ),
            ],
            options={
                "verbose_name": "log detail",
                "verbose_name_plural": "log details",
                "db_table": "django_admin_log_detail",
            },
        ),
    ]

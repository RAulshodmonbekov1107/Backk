# Generated by Django 5.0.4 on 2024-05-07 10:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user_authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BranchAdministrator",
            fields=[
                (
                    "baseuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("user_authentication.baseuser",),
        ),
        migrations.CreateModel(
            name="HospitalAdministrator",
            fields=[
                (
                    "baseuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("user_authentication.baseuser",),
        ),
        migrations.CreateModel(
            name="PatientManager",
            fields=[
                (
                    "standarduser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="user_authentication.standarduser",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("user_authentication.standarduser",),
        ),
        migrations.CreateModel(
            name="Speciality",
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
                ("position", models.CharField(max_length=256)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "standarduser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="user_authentication.standarduser",
                    ),
                ),
                ("is_branch_director", models.BooleanField(default=False)),
                ("is_department_director", models.BooleanField(default=False)),
                (
                    "speciality",
                    models.ManyToManyField(
                        related_name="doctors", to="staff.speciality"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("user_authentication.standarduser",),
        ),
    ]

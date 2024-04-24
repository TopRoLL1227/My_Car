# Generated by Django 5.0.4 on 2024-04-23 07:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("brand_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Cars",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("42896cc2-d4d1-4047-8ee5-9a7a271b3f92"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("model", models.CharField(max_length=100)),
                ("generation", models.CharField(max_length=100)),
                ("engine", models.FloatField(blank=True, null=True)),
                ("year", models.IntegerField(blank=True, null=True)),
                ("horsepower", models.IntegerField(blank=True, null=True)),
                ("kw", models.IntegerField(blank=True, null=True)),
                ("color", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "brand",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_car.brand",
                        verbose_name="brand",
                    ),
                ),
            ],
        ),
    ]

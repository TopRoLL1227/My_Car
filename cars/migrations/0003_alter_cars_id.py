# Generated by Django 5.0.4 on 2024-05-02 15:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_alter_cars_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cars",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("e6e8392e-d761-4289-b268-18ad826bdfcd"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
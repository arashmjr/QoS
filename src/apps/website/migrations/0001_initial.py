# Generated by Django 4.1.3 on 2022-12-14 13:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Website",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("address", models.CharField(max_length=100, verbose_name="address")),
            ],
        ),
    ]

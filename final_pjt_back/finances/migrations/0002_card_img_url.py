# Generated by Django 4.2.7 on 2023-11-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finances", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="img_url",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
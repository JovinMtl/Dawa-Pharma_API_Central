# Generated by Django 5.2.2 on 2025-06-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_medcollection_date_per_alter_medcollection_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="medcollection",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]

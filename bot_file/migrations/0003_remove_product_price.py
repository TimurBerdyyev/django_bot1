# Generated by Django 4.2 on 2024-04-21 09:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bot_file", "0002_telegramuser_alter_category_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="price",
        ),
    ]

# Generated by Django 4.2 on 2024-04-20 15:20

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):
    dependencies = [
        ("bot_file", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TelegramUser",
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
                (
                    "chat_id",
                    models.IntegerField(
                        null=True, unique=True, verbose_name="ID пользователя"
                    ),
                ),
                (
                    "user_login",
                    models.CharField(max_length=255, unique=True, verbose_name="Логин"),
                ),
                (
                    "user_password",
                    models.CharField(max_length=128, verbose_name="Пароль"),
                ),
                (
                    "is_registered",
                    models.BooleanField(default=False, verbose_name="Зарегистрирован"),
                ),
                (
                    "registered_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время регистрации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Телеграмм Пользователь",
                "verbose_name_plural": "Телеграмм Пользователи",
                "db_table": "telegram_users",
                "ordering": ["-registered_at"],
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликован"),
        ),
        migrations.AddField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Время редактирования"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Время создания"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Время создания"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(upload_to="products/", verbose_name="Фотография"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveIntegerField(verbose_name="Цена"),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="bot_file.category",
                verbose_name="Категория",
            ),
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Название подкатегории"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Описание подкатегории"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания подкатегории"
                    ),
                ),
                (
                    "subcategory_category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="bot_file.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подкатегория",
                "verbose_name_plural": "Подкатегории",
                "db_table": "subcategories",
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddField(
            model_name="product",
            name="product_subcategory",
            field=smart_selects.db_fields.ChainedForeignKey(
                auto_choose=True,
                chained_field="product_category",
                chained_model_field="subcategory_category",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="bot_file.subcategory",
                verbose_name="Подкатегория",
            ),
        ),
    ]

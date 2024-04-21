# Generated by Django 4.1.7 on 2023-04-02 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Category ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('description', models.TextField(blank=True, verbose_name='Category Description')),
                ('created_at', models.DateTimeField(verbose_name='Category Created At')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Product ID')),
                ('photo', models.ImageField(upload_to='products/', verbose_name='Product Photo')),
                ('name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('description', models.TextField(blank=True, verbose_name='Product Description')),
                ('price', models.PositiveIntegerField(verbose_name='Product Price')),
                ('created_at', models.DateTimeField(verbose_name='Product Created At')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot_file.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "product_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="ID продукту"
                    ),
                ),
                (
                    "product_name",
                    models.CharField(max_length=256, verbose_name="Назва продукту"),
                ),
                (
                    "product_photo",
                    models.CharField(
                        max_length=1024,
                        null=True,
                        verbose_name="Фото продукту(посилання)",
                    ),
                ),
                (
                    "product_category",
                    models.CharField(max_length=256, verbose_name="Категорія продукту"),
                ),
                (
                    "is_product_of_month",
                    models.BooleanField(
                        default=False, verbose_name="Пропозиція місяця"
                    ),
                ),
                (
                    "is_in_stock",
                    models.BooleanField(default=True, verbose_name="Наявність"),
                ),
                (
                    "is_pickup",
                    models.BooleanField(default=False, verbose_name="Самовивіз"),
                ),
                (
                    "product_description",
                    models.CharField(max_length=2048, verbose_name="Опис продукту"),
                ),
                (
                    "product_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Ціна продукту"
                    ),
                ),
            ],
        ),
    ]
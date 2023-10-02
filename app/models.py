from django.db import models


class Product(models.Model):
    product_id = models.AutoField(verbose_name="ID продукту", primary_key=True)
    product_name = models.CharField(verbose_name="Назва продукту", max_length=256, null=False)
    product_photo = models.CharField(verbose_name="Фото продукту(посилання)", max_length=1024, null=True)
    product_category = models.CharField(verbose_name="Категорія продукту", max_length=256, null=False)
    is_product_of_month = models.BooleanField(verbose_name="Пропозиція місяця", default=False)
    is_in_stock = models.BooleanField(verbose_name="Наявність", default=True)
    is_pickup = models.BooleanField(verbose_name="Самовивіз", default=False)
    product_description = models.CharField(verbose_name="Опис продукту", max_length=2048, null=False)
    product_price = models.DecimalField(verbose_name="Ціна продукту",max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_id}|{self.product_name}|{self.product_price}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.product_id}|{self.product_name})"

    @staticmethod
    def get_by_id(id: int) -> "Product":
        return Product.objects.get(product_id=id)

    @staticmethod
    def get_all():
        return Product.objects.all()



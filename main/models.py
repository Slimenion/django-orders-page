from django.db import models


class Products(models.Model):
    name_product = models.CharField("Название программы", max_length=255)
    price = models.FloatField(max_length=10)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Services(models.Model):
    name_service = models.CharField("Название услуги", max_length=255)
    price = models.FloatField(max_length=10)

    def __str__(self):
        return self.name_service

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Orders(models.Model):
    customers_name = models.CharField("Имя заказчика", max_length=255)
    email = models.EmailField(max_length=254)
    product = models.ForeignKey('Products', on_delete=models.CASCADE,)
    service = models.ForeignKey('Services', on_delete=models.CASCADE,)

    def __str__(self):
        return self.customers_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

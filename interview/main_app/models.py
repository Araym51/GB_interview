from django.db import models

# Create your models here.
"""
3. В каталоге приложения создать модель, которая должна хранить информацию о поступивших товарах:
название, дату поступления, цену, единицу измерения, имя поставщика. Выполнить миграции.
"""


class ProductInformation(models.Model):
    MEASURMENT = (
        (1, 'шт'),
        (2, 'кг')
    )
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "продукты"

    product_name = models.CharField(verbose_name='Название продукта',max_length=256)
    date_of_receipt = models.DateTimeField(verbose_name="дата поступления", auto_now=True)
    price = models.DecimalField(verbose_name="цена", max_digits=8, decimal_places=2)
    units_of_measurement = models.IntegerField(verbose_name="Единица измерения", choices=MEASURMENT)
    provider = models.CharField(verbose_name="Наименование поставщика", max_length=256, blank=True)

    def __str__(self):
        return f'Product: {self.product_name}.'

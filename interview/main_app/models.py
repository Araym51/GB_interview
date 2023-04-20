from django.db import models

# Create your models here.
"""
3. В каталоге приложения создать модель, которая должна хранить информацию о поступивших товарах:
название, дату поступления, цену, единицу измерения, имя поставщика. Выполнить миграции.
"""

class ProductInformation(models.Model):
    product_name = models.CharField(max_length=256)
    date_of_receipt = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    units_of_measurement = models.CharField(max_length=128, null=True, blank=True)
    provider = models.CharField(max_length=256)

    def __str__(self):
        return f'Product: {self.product_name}.'

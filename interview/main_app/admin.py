from django.contrib import admin

from .models import ProductInformation

# Register your models here.
""" 
4. Проверить правильность созданной модели, зарегистрировав ее в админке приложения.
"""


@admin.register(ProductInformation)
class ProductInformation(admin.ModelAdmin):
    list_display = ('product_name', 'date_of_receipt', 'price', 'units_of_measurement', 'provider')
    fields = (('product_name', 'price'), ('date_of_receipt', 'units_of_measurement'), 'provider')
    readonly_fields = ('date_of_receipt',)
    search_fields = ('product_name',)
    ordering = ('-product_name',)

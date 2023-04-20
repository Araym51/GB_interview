from django import forms

from .models import ProductInformation
"""
5. На основе модели добавить класс формы указания данных о товаре. Использовать наследование от forms.ModelForm.
"""

class ProductInformationForm(forms.ModelForm):
    class Meta:
        model = ProductInformation
        fields = ('product_name', 'price', 'units_of_measurement', 'provider')

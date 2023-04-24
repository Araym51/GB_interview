from django import forms

from .models import ProductInformation

"""
5. На основе модели добавить класс формы указания данных о товаре. Использовать наследование от forms.ModelForm.
"""


class ProductInformationForm(forms.ModelForm):
    class Meta:
        model = ProductInformation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductInformationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

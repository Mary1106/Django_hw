from django.forms import ModelForm, BooleanField
from catalog.models import Product
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'

            else:
                field.widget.attrs['class'] = 'form-control'


stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(StyleFormMixin, ModelForm):
    image = forms.ImageField(validators=[FileExtensionValidator(['jpeg', 'png'])])

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'is_published', 'owner')

    def clean_product_name(self):
        product_name = self.cleaned_data['product_name']
        product_name_as_list = product_name.lower().split(' ')
        if set(product_name_as_list).intersection(stop_list):
            raise ValidationError('В названии продукта слово(-а) из стоп-листа!')
        return product_name

    def clean_description(self):
        description = self.cleaned_data['description']
        description_as_list = description.lower().split(' ')
        if set(description_as_list).intersection(stop_list):
            raise ValidationError('В описании продукта слово(-а) из стоп-листа!')
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Цена не может быть нулевой или отрицательной!')
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('is_published',)

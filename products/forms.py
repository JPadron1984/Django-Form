from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'codigo',
            'descripcion',
            'proveedor',
            'precio',
        ]


class RawProductForm(forms.Form):
    codigo = forms.CharField()
    descripcion = forms.CharField()
    proveedor = forms.CharField()
    precio = forms.DecimalField()
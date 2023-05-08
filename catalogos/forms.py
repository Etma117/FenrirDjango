from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['marca', 'nombre', 'categoria', 'modelo', 'descripcion', 'NS', 'existencias', 'precio']  # se añade , 'imagen' para referenciar a la imagen asosiada



from django import forms
from .models import Categoria


class RegisterProduct(forms.Form):
    nombre = forms.CharField(label='Nombre Producto', max_length=100, widget=forms.TextInput(attrs={'class':'w-100', 'autocomplete':'off'}))
    descripcion = forms.CharField(label='Descripcion', max_length=200, widget=forms.Textarea(attrs={'class':'w-100 border-primary', 'autocomplete':'off'}))
    precio = forms.IntegerField(label='Precio', widget=forms.NumberInput(attrs={'class':'w-100', 'autocomplete':'off'}))
    stock = forms.IntegerField(label='Stock', widget=forms.NumberInput(attrs={'class':'w-100', 'autocomplete':'off'}))
    opc_categorias = [(categoria.id_categoria, categoria.titulo) for categoria in Categoria.objects.all()]
    categoria = forms.ChoiceField(choices=opc_categorias, label='Categoría:', widget=forms.Select(attrs={'class':'w-100'}))



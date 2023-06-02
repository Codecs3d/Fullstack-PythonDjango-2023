from django import forms
from Web.data import regiones
class RegisterForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', max_length=100, widget=forms.EmailInput(attrs={'class':'w-100'}))
    f_name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class':'w-100'}))
    l_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'class':'w-100'}))
    phone = forms.CharField(label='Celular', max_length=9, widget=forms.NumberInput(attrs={'class':'w-100'}))
    street = forms.CharField(label='Calle', max_length=100, widget=forms.TextInput(attrs={'class':'w-100'}))
    number = forms.CharField(label='Número', max_length=100, widget=forms.NumberInput(attrs={'class':'w-100'}))
    region = forms.ChoiceField(choices=regiones, label='Región', widget=forms.Select(attrs={'class':'w-100'}))
    fecha_nac = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

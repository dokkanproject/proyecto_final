from django import forms
from django.forms import TextInput

class ProductoFormularioBase(forms.Form):
    producto    = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': '* ingrese el Producto', 'style': 'width: 100%;', 'class': 'form-control'}))
    marca       = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': '* ingrese la marca', 'style': 'width: 100%;', 'class': 'form-control'}))
    precio      = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '* ingrese el Precio', 'style': 'width: 100%;', 'class': 'form-control'}))
    stock       = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '* ingrese el Stock', 'style': 'width: 100%;', 'class': 'form-control'}))
    fecha       = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
class crearFormulario(ProductoFormularioBase):...
    
class buscarFormulario(forms.Form):
    producto    = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': '* ingrese el Producto', 'style': 'width: 100%;', 'class': 'form-control'}))

class EditarFormulario(ProductoFormularioBase):...
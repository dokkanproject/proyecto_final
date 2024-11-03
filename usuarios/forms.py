from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormCreateUser(UserCreationForm):
    email       = forms.EmailField()
    password1   = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2   = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    first_name  = forms.CharField(label='Nombre')
    last_name   = forms.CharField(label='Apellido')
    
    class Meta:
        model       = User
        fields      = ['username','email','first_name','last_name','password1','password2']
        help_texts  = {key: '' for key in fields}
        
class FormEditPerfil(UserChangeForm):
    email       = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    first_name  = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    last_name   = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    password    = None
    avatar      = forms.ImageField(required=False, widget=forms.FileInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    
    class Meta:
        model   = User
        fields  = ['email','first_name','last_name','avatar']
        help_texts  = {key: '' for key in fields}

class UsuariosFormularioBase(forms.Form):
    email       = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    first_name  = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    last_name   = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    
class buscarFormulario(forms.Form):
    usuarios    = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': '* ingrese el Usuario', 'style': 'width: 100%;', 'class': 'form-control'}))
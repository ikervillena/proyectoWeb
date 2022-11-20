from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateInput

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="nombre", max_length=40, widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    usuario = forms.CharField(label="usuario", max_length=60, widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    contrasenya = forms.CharField(label="contrasenya", max_length=60, widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(label="email", required=False, widget=forms.EmailInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))

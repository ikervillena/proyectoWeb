from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateInput

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=40, widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    usuario = forms.CharField(label="Usuario", max_length=60, widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    contrasenya = forms.CharField(label="Contrasenya", max_length=60, widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(label="Email", required=False, widget=forms.EmailInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))

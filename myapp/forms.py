from django import forms

class UsuarioForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")
from django import forms
from .models import *


class BusquedaForm(forms.Form):
    terminodebusqueda = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control my-2'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))

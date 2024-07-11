from django import forms
from .models import *


class BusquedaForm(forms.Form):
    terminodebusqueda = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput({'placeholder':'Password'}))


class SingupForm(forms.Form):
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    lastname= forms.CharField(max_length=50, widget=forms.TextInput({'placeholder':'Last Name'}))
    email =forms.CharField(max_length=50, widget=forms.TextInput({'placeholder':'Email'}))
    password=forms.CharField(max_length=50, widget=forms.PasswordInput({'placeholder':'Password'}))
    confirmpassword=forms.CharField(max_length=50, widget=forms.PasswordInput({'placeholder':'Confirm Password'}))


class CrearperfilForm(forms.Form):
    mision = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':''}))
    vision = forms.CharField(max_length=50, widget=forms.TextInput({'placeholder':''}))
    imagen_empresa =forms.ImageField(widget=forms.FileInput())
    servicios =forms.CharField(max_length=50, widget=forms.TextInput({'placeholder':''}))
    categoria=forms.CharField(max_length=50, widget=forms.TextInput({'placeholder':''}))
    
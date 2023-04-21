from django import forms
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio


class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio



class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [ 'user_name', 'password', 'name', 'surname']
        widgets = {'password': forms.PasswordInput()}



class PublicationsForm(forms.Form):
    user_name = forms.EmailField()
    date_publication = forms.DateField()
    publication = forms.CharField(max_length=50)
    price_publication = forms.IntegerField()
    publication_sell = forms.BooleanField()


class PurchasesForm(forms.Form):
    user_name = forms.EmailField()
    date_purchase = forms.DateField()
    purchase = forms.CharField(max_length=50)
    price_purchase = forms.IntegerField()





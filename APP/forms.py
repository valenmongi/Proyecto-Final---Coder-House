from django import forms
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="User Email")
    password1=forms.CharField(label="Password", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio


class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="User Email")
    password1= forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirm new Password", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Change Name')
    last_name=forms.CharField(label='Change Surname')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio



class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class ProjectsForm(forms.Form):
    title = forms.CharField()
    subtitle = forms.CharField()
    description = forms.CharField()
    #project_manager = forms.CharField()
    user_in_charge = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    completed = forms.BooleanField()


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





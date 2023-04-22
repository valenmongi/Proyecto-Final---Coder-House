from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF  
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS   
# Create your views here.

def index(request):
    params = {}

    return render(request,'APP/index.html',params)

def about_me(request):
    params = {}

    return render(request,'APP/aboutMe.html',params)

#login logout register

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)#verifica si el usuario existe, si existe, lo devuelve, y si no devuelve None 
            
            if usuario is not None:
                login(request, usuario)
                return render(request, "APP/index.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "APP/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "APP/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "APP/login.html", {"form": form})




def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "APP/index.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "APP/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "APP/register.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "APP/index.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "APP/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "APP/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})


#NEW VIEWS

def project_new(request):
    params = {}

    # User sends data to server
    if request.method == 'POST':

        form = ProjectsForm(request.POST)

        #Data valid
        if form.is_valid():

            _title = form.cleaned_data['title']
            _sub_title = form.cleaned_data['subtitle']
            _description = form.cleaned_data['description']
            _user_in_charge = form.cleaned_data['user_in_charge']
            _start_date = form.cleaned_data['start_date'] 
            _end_date = form.cleaned_data['end_date']
            _image = form.cleaned_data['image']
            _completed = form.cleaned_data['completed']
            
            

            _newProject = Project(title = _title, 
                                 subtitle = _sub_title, 
                                 description = _description,
                                 user_in_charge = _user_in_charge,
                                 start_date = _start_date,
                                 end_date = _end_date,
                                 image = _image,
                                 completed = _completed,
                                                              
                                )

            _newProject.save()

            return render(request,'APP/new_project.html',params)

        
        #Data no valid
        else:
            
            params['form'] = form

            return render(request,'APP/new_project.html',params)


    # User asks data to server
    else:
        
        form = ProjectsForm()
        
        params['form'] = form

        return render(request,'APP/new_project.html',params)

"""
def projects(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST) 
        if form.is_valid():
            pro = Project()
            pro.title = form.cleaned_data['title']
            pro.subtitle = form.cleaned_data['subtitle']
            pro.description = form.cleaned_data['description']
            pro.user_in_charge = form.cleaned_data['user_in_charge']
            pro.start_date = form.cleaned_data['start_date']
            pro.end_date = form.cleaned_data['end_date']
            pro.completed = form.cleaned_data['completed']
            pro.save()
            form = ProjectsForm()
        else:
            pass
    else:
        form = ProjectsForm()
    
    projects = Project.objects.all()
    context = {"projects":projects, "form":form}
    return render(request, 'APP/new_project.html', context)
"""


def projects_view(request):
    params = {}

    if request.method == 'POST':

        form = ProjectsForm(request.POST)

        _title = request.POST['title']
        _sub_title = request.POST['subtitle']
        _description = request.POST['description']
        _user_in_charge = request.POST['user_in_charge']
        _start_date = request.POST['start_date']
        _end_date = request.POST['end_date']
        #_completed = request.POST['completed']


        params['projects_search'] = Project.objects.filter(
            title__icontains = _title,
            subtitle__icontains = _sub_title,
            description__icontains = _description,
            user_in_charge__icontains = _user_in_charge,
            start_date__icontains = _start_date,
            end_date__icontains = _end_date,
            #completed__icontains = _completed,

        )

        params['form'] = form

        return render(request,'APP/search_project.html',params)
    
    else:
        
        form = ProjectsForm()
        
        params['projects_search'] = Project.objects.all()
        params['form'] = form

    return render(request,'APP/search_project.html',params)


#OLD VIEWS

def publications(request):
    if request.method == 'POST':
        form = PublicationsForm(request.POST) 
        if form.is_valid():
            publ = Publications()
            publ.user_name = form.cleaned_data['user_name']
            publ.date_publication = form.cleaned_data['date_publication']
            publ.publication = form.cleaned_data['publication']
            publ.price_publication = form.cleaned_data['price_publication']
            publ.publication_sell = form.cleaned_data['publication_sell']
            publ.save()
            form = PublicationsForm()
        else:
            pass
    else:
        form = PublicationsForm()
    
    publications = Publications.objects.all()
    context = {"publications":publications, "form":form}
    return render(request, 'APP/publications.html', context)

def publications_view(request):
    params = {}

    if request.method == 'POST':

        form = PublicationsForm(request.POST)

        _user_name = request.POST['user_name']
        _date_publication = request.POST['date_publication']
        _publication = request.POST['publication']
        _price = request.POST['price_publication']
        _is_sell = request.POST['publication_sell'] 


        params['publications_search'] = Publications.objects.filter(
            user_name__icontains = _user_name,
            date_publication__icontains = _date_publication,
            publication__icontains = _publication,
            price_publication__icontains = _price,
            publication_sell__icontains = _is_sell,

        )

        params['form'] = form

        return render(request,'APP/publications_search.html',params)
    
    else:
        
        form = PublicationsForm()
        
        params['publications_search'] = Publications.objects.all()
        params['form'] = form

    return render(request,'APP/publications_search.html',params)



def users(request):
    if request.method == 'POST':
        form = UsersForm(request.POST) 
        if form.is_valid():
            user = Users()
            user.user_name = form.cleaned_data['user_name']
            user.password = form.cleaned_data['password']
            user.name = form.cleaned_data['name']
            user.surname = form.cleaned_data['surname']
            user.save()
            form = UsersForm()
        else:
            pass
    else:
        form = UsersForm()
    
    user = Users.objects.all()
    context = {"users":user, "form":form}
    return render(request, 'APP/users.html', context)


def purchases(request):
    if request.method == 'POST':
        form = PurchasesForm(request.POST) 
        if form.is_valid():
            purch = Purchases()
            purch.user_name = form.cleaned_data['user_name']
            purch.date_purchase = form.cleaned_data['date_purchase']
            purch.purchase = form.cleaned_data['purchase']
            purch.price_purchase = form.cleaned_data['price_purchase']
            purch.save()
            form = PurchasesForm()
        else:
            pass
    else:
        form = PurchasesForm()
    
    purchases = Purchases.objects.all()
    context = {"purchases":purchases, "form":form}
    return render(request, 'APP/purchase.html', context)


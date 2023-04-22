from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    path("", index, name="index"),
    path("publications/", publications, name="publications"),
    path("users/", users, name="users"),
    path("purchase/", purchases, name="purchases"),
    path("publications_search/", publications_view, name="publications_search"),

    #NEW URLS
    path("new_project/", project_new, name="new_project"), 
    path("search_project/", projects_view, name="search_project"),


    #LOGIN URLs
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('aboutMe/', about_me,name='about_me'), # type: ignore

    
    
] 
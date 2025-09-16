from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Pelicula
from .forms import PeliculaForm

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect("lista_peliculas")
        except IntegrityError:
            return render(request, "signup.html", {"form": UserCreationForm(), "error": "El nombre de usuario ya existe."})

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("lista_peliculas")
        return render(request, "signin.html", {"form": AuthenticationForm(), "error": "Usuario o contraseña incorrecta."})

def signout(request):
    logout(request)
    return redirect("home")

def lista_peliculas(request):
    peliculas = Pelicula.objects.filter(usuario=request.user)
    return render(request, "lista_peliculas.html", {"peliculas": peliculas})

def crear_pelicula(request):
    if request.method == 'GET':
        return render(request, 'crear_pelicula.html', {'form': PeliculaForm()})
    else:
        form = PeliculaForm(request.POST)
        if form.is_valid():
            pelicula = form.save(commit=False)
            pelicula.usuario = request.user
            pelicula.save()
            return redirect('lista_peliculas')
        return render(request, 'crear_pelicula.html', {'form': form, 'error': 'Datos inválidos.'})
    
    
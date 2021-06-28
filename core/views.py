from django.shortcuts import render, redirect, get_object_or_404
from .models import post, categoria
from .forms import contactoForm, addForm

# Create your views here.

def home(request):
        
        posts = post.objects.all()
        categorias = categoria.objects.all()
        data = { 
                'posts': posts,
                'formContacto': contactoForm(),
                'categorias': categorias
        }

        if request.method == 'POST':
                formulario = contactoForm(data=request.POST)
                if formulario.is_valid():
                        formulario.save()
                        data ["mensaje"]= "mensaje enviado"
                else:
                        data["formContacto"] = formulario
        return render(request, 'core/home.html', data)

def login(request):

        return render(request, 'core/login.html')


def signup(request): 

        return render(request, 'core/signup.html')


def contacto(request): 

        data = {
                'formContacto': contactoForm()
        }
 
        if request.method == 'POST':
                formulario = contactoForm(data=request.POST)
                if formulario.is_valid():
                        formulario.save()
                        data ["mensaje"]= "mensaje enviado"
                else:
                        data["formContacto"] = formulario

        return render(request, 'core/contacto.html', data)


def detalle(request, id): 

        categorias = categoria.objects.all()
        detalleP = get_object_or_404(post, id=id)

        data = {
                'detalleP':detalleP,
                'categorias': categorias
        }

        return render(request, 'core/detalle.html', data)
        

def feed(request): 

        posts = post.objects.all()
        categorias = categoria.objects.all()
        data = { 
                'posts': posts,
                'categorias': categorias
        }

        return render(request, 'core/feed.html', data)

def agregar(request):

        data = {
                'formAdd': addForm()
        }

        if request.method  == 'POST':
                formularioAdd = addForm(data=request.POST, files=request.FILES)
                if formularioAdd.is_valid():
                        formularioAdd.save()
                        data["mensaje"] = "Agregado correctamente"
                else:
                        data["formAdd"] = formularioAdd

        return render(request, 'core/agregar.html', data)

def listar(request):

        posts = post.objects.all()

        data = {
                'posts' : posts
        }

        return render(request, 'core/listar.html', data)


def editar(request, id):

        poste = get_object_or_404(post, id=id)

        data = {
                'formAdd': addForm(instance=poste)
        }

        if request.method == 'POST':
                formularioEdit = addForm(data=request.POST, files=request.FILES, instance=poste)
                if formularioEdit.is_valid():
                        formularioEdit.save()
                        return redirect(to="listar")
                data["formAdd"] = formularioEdit


        return render(request, 'core/editar.html', data)

def eliminar(request, id):
        
        poste = get_object_or_404(post, id=id)
        poste.delete()
        return redirect(to="listar")
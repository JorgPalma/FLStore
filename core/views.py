from django.shortcuts import render
from .models import post
from .forms import contactoForm, addForm

# Create your views here.

def home(request):
        
        posts = post.objects.all()
        data = { 
                'posts': posts,
                'formContacto': contactoForm()
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


def detalle(request): 

        return render(request, 'core/detalle.html')
        

def feed(request): 

        return render(request, 'core/feed.html')

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
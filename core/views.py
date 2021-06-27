from django.shortcuts import render
from .models import post

# Create your views here.

def home(request):
        
        posts = post.objects.all()
        data = { 
                'posts': posts
        }
        return render(request, 'core/home.html', data)

def login(request):

        return render(request, 'core/login.html')


def signup(request): 

        return render(request, 'core/signup.html')


def contacto(request): 

        return render(request, 'core/contacto.html')


def detalle(request): 

        return render(request, 'core/detalle.html')
        

def feed(request): 

        return render(request, 'core/feed.html')
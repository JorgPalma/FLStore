from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'core/home.html')

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
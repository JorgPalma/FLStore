from django.shortcuts import render

# Create your views here.

def home(request):

    contexto={"nombre":"Jorge",
            "edad":"24"}

    return render(request, 'core/home.html', contexto)

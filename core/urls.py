from django.urls import path
from .views import home, login, contacto, detalle, signup, feed, agregar, listar

urlpatterns=[
        path('', home, name="home"),
        path('login/', login, name="login"),
        path('contacto/', contacto, name="contacto"),
        path('detalle/', detalle, name="detalle"),
        path('signup/', signup, name="signup"),
        path('feed/', feed, name="feed"),
        path('agregar/', agregar, name="agregar"),
        path('listar/', listar, name="listar")
]
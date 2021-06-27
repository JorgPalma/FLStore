from django.contrib import admin
from .models import categoria, post, contacto

# Register your models here.

admin.site.register(categoria)
admin.site.register(post)
admin.site.register(contacto)
from django.db import models
from django.db.models.fields import NullBooleanField

# Create your models here.
class categoria(models.Model):
    nombreCat = models.CharField(verbose_name="Nombre categoria", max_length=20)

    def __str__(self):
        return self.nombreCat

class post(models.Model):
    nombreP = models.CharField(verbose_name="Nombre producto", max_length=25)
    descripcionP = models.CharField(verbose_name="Descipcion producto", max_length=700)
    miniDescripcion = models.CharField(verbose_name="Descripcion abreviada", max_length=30)
    precioP = models.IntegerField(verbose_name="Precio producto")
    nombreU = models.CharField(verbose_name="Nombre de usuario", max_length=20)
    emailU = models.CharField(verbose_name="Correo de usuario", max_length=30)
    telefonoU = models.CharField(verbose_name="Teléfono de usuario", max_length=12, blank=True)
    instagramU = models.CharField(verbose_name="Instagram de usuario", max_length=20, blank=True)
    facebookU = models.CharField(verbose_name="Facebook de usuario", max_length=25, blank=True)
    twitterU = models.CharField(verbose_name="Twitter de usuario", max_length=25, blank=True)
    whatsappU = models.CharField(verbose_name="Whatsapp de usuario", max_length=12, blank=True)
    categoriaP = models.ForeignKey(categoria, on_delete=models.CASCADE)
    imgP = models.ImageField(upload_to="productos", null=True, verbose_name="Imagen producto")

    def __str__(self):
        return f"Usuario: {self.nombreU}, Post: {self.nombreP}"

class contacto(models.Model):
    nombreC = models.CharField(verbose_name="Nombre de contacto", max_length=20)
    correoC = models.EmailField(verbose_name="Correo de contacto")
    mensajeC = models.TextField(verbose_name="Mensaje de contacto")

    def __str__(self):
        return f"Usuario: {self.nombreC}"
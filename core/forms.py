from django import forms
from .models import contacto, post


class contactoForm(forms.ModelForm):

    nombreC = forms.CharField(label='Nombre de usuario' ,widget=forms.TextInput(attrs={"placeholder": "Nombre"}))
    correoC = forms.EmailField(label='Correo electrónico' ,widget=forms.TextInput(attrs={"placeholder": "ejemplo@mail.com"}))
    mensajeC = forms.CharField(label='Mensaje' ,widget=forms.Textarea(attrs={"placeholder": "Mensaje a enviar..."}))

    class Meta:
        model = contacto
        fields = '__all__'

class addForm(forms.ModelForm):

    nombreP = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nombre del producto...", "class": "add-form-default"}))
    descripcionP = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Descripción del producto...", "class": "add-form-default"}))
    miniDescripcion = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Descripción abreviada...", "class": "add-form-default"}))
    precioP = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Precio...", "class": "add-form-especial"})) 
    nombreU = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nombre de usuario...", "class": "add-form-especial"}))
    emailU = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Correo electrónico...", "class": "add-form-especial"}))
    instagramU = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Instagram...", "class": "add-form-especial"}))
    twitterU = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Twitter..", "class": "add-form-especial"}))
    facebookU = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Facebook...", "class": "add-form-especial"}))
    telefonoU = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Teléfono...", "class": "add-form-especial"}))
    whatsappU = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Whatsapp...", "class": "add-form-especial"}))

    class Meta:
        model = post
        fields = '__all__'
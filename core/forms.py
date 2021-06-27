from django import forms
from .models import contacto


class contactoForm(forms.ModelForm):

    nombreC = forms.CharField(label='Nombre de usuario' ,widget=forms.TextInput(attrs={"placeholder": "Nombre"}))
    correoC = forms.EmailField(label='Correo electrónico' ,widget=forms.TextInput(attrs={"placeholder": "ejemplo@mail.com"}))
    mensajeC = forms.CharField(label='Mensaje' ,widget=forms.Textarea(attrs={"placeholder": "Mensaje a enviar..."}))

    class Meta:
        model = contacto
        fields = '__all__'
from django import forms

from usuarios.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
    Esta clase hereda de UserCreationForm
    UserCreationForm contiene usernamme, password1 y password2
    Se le agrega email

    """
    email = forms.EmailField(
        max_length=254,
        help_text="Required. Inform a valid email address.",
        )
    nombre= forms.CharField(
        max_length=50,
        help_text="Requerido",
        )
    apellido = forms.CharField(
        max_length=50,
        help_text="Requerido"
    )
    numero_de_telefono= forms.CharField(
        max_length=15,
    )
    address = forms.CharField(
        max_length=15, 
    )

    

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

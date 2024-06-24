from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import CustomUser

class RegistrationForm(UserCreationForm):
    """
    Formulario personalizado de registro que extiende UserCreationForm
    """

    email = forms.EmailField(
        max_length=254,
        help_text="Requerido. Ingresa una dirección de correo electrónico válida.",
        label="Correo Electrónico"
    )

    nombre = forms.CharField(
        max_length=50,
        help_text="Requerido. Ingresa tu nombre.",
        label="Nombre"
    )

    apellido = forms.CharField(
        max_length=50,
        help_text="Requerido. Ingresa tu apellido.",
        label="Apellido"
    )

    numero_de_telefono = forms.CharField(
        max_length=15,
        help_text="Ingresa tu número de teléfono.",
        label="Número de Teléfono"
    )

    address = forms.CharField(
        max_length=255,
        help_text="Ingresa tu dirección.",
        label="Dirección"
    )

    username = forms.CharField(
        max_length=150,
        help_text="Requerido. Ingresa un nombre de usuario.",
        label="Nombre de Usuario"
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'nombre', 'apellido', 'numero_de_telefono', 'address', 'password1', 'password2')
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'nombre', 'apellido', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'nombre', 'apellido')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('nombre', 'apellido', 'email', 'numero_de_telefono', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombre', 'apellido', 'numero_de_telefono', 'address', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # Cuando se está creando un nuevo usuario
            if CustomUser.objects.filter(username=obj.username).exists():
                raise ValidationError('Ya existe un usuario con este nombre de usuario.')
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from usuario.models import Usuario
from django.contrib.auth.models import Permission


class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'nombres',
        'apellidos',
        'grupo',
        'is_active',
        'is_staff',
        'is_superuser',

    )
    search_fields=['id_usuario']


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Permission)
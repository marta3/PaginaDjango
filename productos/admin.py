from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from productos.models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PerfilInline(admin.StackedInline):
    model = Perfiles
    can_delete = False
    verbose_name_plural = 'perfil'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline, )


admin.site.register(Perfiles)
admin.site.register(Productos)
admin.site.register(Pedidos)
admin.site.register(Carrito)
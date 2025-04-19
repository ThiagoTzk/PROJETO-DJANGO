from django.contrib import admin
from .models import Usuario, Quarto

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'endereco')
    search_fields = ('titulo', 'descricao', 'endereco')

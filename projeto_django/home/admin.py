from django.contrib import admin
from .models import Usuario, Quarto

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'telefone')}),
        ('Tipo de Conta', {'fields': ('user_type',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Dados Acadêmicos', {
            'fields': ('faculdade', 'curso', 'matricula'),
            'classes': ('collapse',),
            'description': 'Apenas para locatários'
        }),
    )

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'proprietario', 'preco', 'data_disponivel', 'criado_em')
    list_filter = ('proprietario', 'data_disponivel', 'criado_em')
    search_fields = ('titulo', 'descricao', 'endereco')
    raw_id_fields = ('proprietario',)
    date_hierarchy = 'criado_em'
    ordering = ('-criado_em',)
    
    fieldsets = (
        (None, {'fields': ('titulo', 'descricao')}),
        ('Localização', {'fields': ('endereco', 'preco')}),
        ('Datas', {'fields': ('data_disponivel', 'criado_em')}),
        ('Mídia', {'fields': ('imagem',)}),
        ('Proprietário', {'fields': ('proprietario',)}),
    )
    
    readonly_fields = ('criado_em',)
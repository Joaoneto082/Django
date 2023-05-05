from django.contrib import admin

from .models import Curso, Avaliacao, Contato

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'criacao', 'atualizacao', 'ativo')
    
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    pass


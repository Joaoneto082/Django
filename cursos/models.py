from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = _('Avaliação')
        verbose_name_plural = _('Avaliações')
        unique_together = ['email', 'curso']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com a nota {self.avaliacao}'

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Contato {self.id}: {self.mensagem[:50]}..."

    

# class Contato(models.Model):
#     nome = models.CharField(max_length=100)
#     email = models.EmailField()
#     telefone = models.CharField(max_length=20)
#     mensagem = models.TextField()
#     data_envio = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.nome

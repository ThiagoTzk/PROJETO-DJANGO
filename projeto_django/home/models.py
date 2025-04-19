# home/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='usuarios/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Quarto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    endereco = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='quartos/', blank=True, null=True)
    proprietario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='quartos'
    )

    def __str__(self):
        return self.titulo
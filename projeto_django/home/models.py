from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('Locador', 'Locador'),
        ('Locatario', 'Locatário'),
    )
    
    user_type = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='Locatario'
    )
    telefone = models.CharField(max_length=20, blank=True)
    faculdade = models.CharField('Faculdade', max_length=100, blank=True)
    curso = models.CharField('Curso', max_length=100, blank=True)
    matricula = models.CharField('Matrícula', max_length=20, blank=True)
    foto = models.ImageField(
        'Foto de Perfil',
        upload_to='perfil/',
        blank=True,
        null=True,
        default='perfil/default.png'
    )
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Quarto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    endereco = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    proprietario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='quartos',
        limit_choices_to={'user_type': 'Locador'}
    )
    imagem = models.ImageField(upload_to='quartos/', blank=True, null=True)
    data_disponivel = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
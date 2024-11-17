from django.db import models
from datetime import datetime
from django.conf import settings



class Post(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    ano_foto = models.IntegerField()
    data_postagem = models.DateTimeField(default=datetime.now)
    url_foto = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.titulo} ({self.ano_foto})'


class Comentario(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    foto = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_postagem = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f'"{self.texto}" - {self.autor.username}'

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    fotos = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.nome}'
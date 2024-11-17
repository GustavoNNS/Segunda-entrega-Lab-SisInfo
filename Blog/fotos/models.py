from django.db import models

from django.conf import settings

'''
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    ano_foto = models.IntegerField()
    data_postagem = models.DateTimeField()
    url_foto = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.titulo} ({self.ano_foto})'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
'''
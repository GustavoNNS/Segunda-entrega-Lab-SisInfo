from django.forms import ModelForm
from .models import Post, Comentario


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'descricao',
            'ano_foto',
            'url_foto',
        ]
        labels = {
            'titulo': 'Título',
            'ano_foto': 'Data da fotografia',
            'descricao': 'Descrição da foto',
            'url_foto': 'URL da fotografia',
        }
class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'autor',
            'texto',
        ]
        labels = {
            'autor': 'Usuário',
            'texto': 'Comentário',
        }
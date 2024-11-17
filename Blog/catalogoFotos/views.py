from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comentario, Categoria
from .forms import PostForm, ComentarioForm
from django.views import generic, View
from django.urls import reverse_lazy

class catalogo_fotos_listView(generic.ListView):
    model = Post
    template_name = 'catalogoFotos/index.html'

class detail_foto_detailView(generic.DetailView):
    model = Post
    template_name = 'catalogoFotos/detail.html'
    def get(self, request, foto_id):
        foto = get_object_or_404(Post, pk=foto_id)
        context = {'foto': foto}
        return render(request, 'catalogoFotos/detail.html', context)

def busca_fotos(request):
    context = {}
    if request.GET.get('query', False):
        lista_fotos = Post.objects.filter(titulo__icontains = request.GET['query'].lower())
        context = {"lista_fotos" : lista_fotos}
    return render(request, 'catalogoFotos/busca.html', context)
from django.http import HttpResponseRedirect
from django.urls import reverse

class postar_foto_createView(View):
    def get(self, request):
        form = PostForm()
        context = {'form' : form}
        return render(request, 'catalogoFotos/postar.html', context)
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form_titulo = form.cleaned_data['titulo']
            form_descricao = form.cleaned_data['descricao']
            form_ano_foto = form.cleaned_data['ano_foto']
            form_url_foto = form.cleaned_data['url_foto']
            foto = Post(titulo = form_titulo,
                        descricao = form_descricao,
                        ano_foto = form_ano_foto,
                        url_foto = form_url_foto)
            foto.save()
            return HttpResponseRedirect(reverse('catalogo:detail', args=(foto.id,)))
        return HttpResponseRedirect(reverse('catalogo:index'))

class atualizar_post_updateView(View):
    def get(self, request, foto_id):
        foto = get_object_or_404(Post, pk=foto_id)
        form = PostForm(
            initial={
                'titulo': foto.titulo,
                'descricao' : foto.descricao,
                'ano_foto': foto.ano_foto,
                'url_foto': foto.url_foto
            })
        context = {'foto': foto, 'form':form}
        return render(request, 'catalogoFotos/atualizar.html', context)
    def post(self,request, foto_id):
        foto = get_object_or_404(Post, pk=foto_id)
        form = PostForm(request.POST)
        if form.is_valid():
            foto.titulo = form.cleaned_data['titulo']
            foto.descricao = form.cleaned_data['descricao']
            foto.ano_foto = form.cleaned_data['ano_foto']
            foto.url_foto = form.cleaned_data['url_foto']
            foto.save()
            return HttpResponseRedirect(
                reverse('catalogo:detail', args=(foto.id, )))
        
class deletar_foto_deleteView(View):
    def get(self,request, foto_id):
        foto = get_object_or_404(Post, pk=foto_id)
        context = {'foto': foto}
        return render(request, 'catalogoFotos/deletar.html', context)
    def post(self,request,foto_id):
        foto = get_object_or_404(Post, pk=foto_id)
        foto.delete()
        return HttpResponseRedirect(reverse('catalogo:index'))

def criar_comentario(request, foto_id):
    foto = get_object_or_404(Post, pk=foto_id)
    if request.method == 'POST':

        form = ComentarioForm(request.POST)
        if form.is_valid():
            autor_form = form.cleaned_data['autor']
            texto_form = form.cleaned_data['texto']
            comentario = Comentario(autor=autor_form,
                            texto=texto_form,
                            foto=foto)
            comentario.save()
            return HttpResponseRedirect(
                reverse('catalogo:detail', args=(foto_id,)))
        pass
    else:
        
        form = ComentarioForm()
    context = {'form': form, 'foto': foto}
    return render(request, 'catalogoFotos/comentario.html', context)

class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = 'catalogoFotos/categorias.html'


class CategoriaCreateView(generic.CreateView):
    model = Categoria
    template_name = 'catalogoFotos/criarCategoria.html'
    fields = ['nome', 'descricao', 'fotos']
    success_url = reverse_lazy('catalogo:categorias')

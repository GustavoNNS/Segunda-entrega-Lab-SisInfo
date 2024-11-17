from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.views import generic, View

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
            return HttpResponseRedirect(reverse('catalogo:detail', args=(foto.id, )))

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

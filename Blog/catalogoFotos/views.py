from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def catalogo_fotos(request):
    context = {"lista_fotos": Post.objects.all() }
    return render(request, 'catalogoFotos/index.html', context)

def detail_foto(request, foto_id):
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

def postar_foto(request):
    if request.method == 'POST':
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
    else:
        form = PostForm()
        context = {'form' : form}
        return render(request, 'catalogoFotos/postar.html', context)
    
def atualizar_post(request, foto_id):
    foto = get_object_or_404(Post, pk=foto_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            foto.titulo = form.cleaned_data['titulo']
            foto.descricao = form.cleaned_data['descricao']
            foto.ano_foto = form.cleaned_data['ano_foto']
            foto.url_foto = form.cleaned_data['url_foto']
            foto.save()
            return HttpResponseRedirect(
                reverse('catalogo:detail', args=(foto.id, )))
    else:
        form = PostForm(
            initial={
                'titulo': foto.titulo,
                'descricao' : foto.descricao,
                'ano_foto': foto.ano_foto,
                'url_foto': foto.url_foto
            })
        context = {'foto': foto, 'form':form}
        return render(request, 'catalogoFotos/atualizar.html', context)

def deletar_foto(request, foto_id):
    foto = get_object_or_404(Post, pk=foto_id)

    if request.method == "POST":
        foto.delete()
        return HttpResponseRedirect(reverse('catalogo:index'))
    context = {'foto': foto}
    return render(request, 'catalogoFotos/deletar.html', context)

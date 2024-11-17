from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import datetime

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
        foto = Post(titulo = request.POST['titulo'],
                    descricao = request.POST["descricao"],
                    ano_foto = request.POST['ano_foto'],
                    url_foto = request.POST['url_foto'])      
        foto.save()
        return HttpResponseRedirect(
            reverse('catalogo:detail', args=(foto.id, )))
    else:
        return render(request, 'catalogoFotos/postar.html', {})
    
def atualizar_post(request, foto_id):
    foto = get_object_or_404(Post, pk=foto_id)

    if request.method == "POST":
        foto.titulo = request.POST['titulo']
        foto.descricao = request.POST["descricao"]
        foto.ano_foto = int(request.POST['ano_foto'])
        foto.url_foto = request.POST['url_foto']
        foto.save()
        return HttpResponseRedirect(
            reverse('catalogo:detail', args=(foto.id, )))

    context = {'foto': foto}
    return render(request, 'catalogoFotos/atualizar.html', context)

def deletar_foto(request, foto_id):
    foto = get_object_or_404(Post, pk=foto_id)

    if request.method == "POST":
        foto.delete()
        return HttpResponseRedirect(reverse('catalogo:index'))
    context = {'foto': foto}
    return render(request, 'catalogoFotos/deletar.html', context)

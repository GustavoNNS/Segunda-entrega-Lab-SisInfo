from django.shortcuts import render
from django.http import HttpResponse
from .tempdata import foto_data

def detail_foto(request, foto_id):
    context = {'foto': foto_data[foto_id - 1]}
    return render(request, 'catalogoFotos/detail.html', context)

def catalogo_fotos(request):
    context = {"lista_fotos": foto_data }
    return render(request, 'catalogoFotos/index.html', context)

def busca_fotos(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "lista_fotos": [
                f for f in foto_data
                if request.GET['query'].lower() in f['titulo'].lower()
            ]
        }
    return render(request, 'catalogoFotos/busca.html', context)
from django.http import HttpResponseRedirect
from django.urls import reverse

def postar_foto(request):
    if request.method == 'POST':
        foto_data.append({
            'titulo': request.POST['titulo'],
            'ano_foto': request.POST['ano_foto'],
            'foto_url': request.POST['foto_url']
        })
        return HttpResponseRedirect(
            reverse('catalogo:detail', args=(len(foto_data), )))
    else:
        return render(request, 'catalogoFotos/postar.html', {})


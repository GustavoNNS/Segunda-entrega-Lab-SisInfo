from django.shortcuts import render
from django.http import HttpResponse
from .tempdata import foto_data

def detail_foto(request, foto_id):
    context = {'foto': foto_data[foto_id - 1]}
    return render(request, 'catalogoFotos/detail.html', context)
def catalogo_fotos(request):
    context = {"lista_fotos": foto_data }
    return render(request, 'catalogoFotos/index.html', context)


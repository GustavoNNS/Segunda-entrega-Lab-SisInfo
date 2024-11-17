from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post

def index(request):
    posts_lista = {}
    context = {'posts_lista': posts_lista}
    return render(request, 'fotos/index.html', context)


def about(request):
    context = {}
    return render(request, 'fotos/about.html', context)

def detail_foto(request):
    pass

def lista_fotos(request):
    lista = []
    context = {'lista' : lista}
    return render(request, 'fotos/index.html', context)

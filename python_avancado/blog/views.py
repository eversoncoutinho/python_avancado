from django.shortcuts import render
from django.http import HttpResponse
from blog import models #ou
from .models import Anuncio, Categoria

def home(request):

    anuncio = Anuncio.objects.all() #toda vez que eu visitar a home vai rodar esse código
    categoria = Categoria.objects.all() #pega todos os objetos do banco de dados
    
    print(Anuncio)


    return render(request, 'home.html', {'anuncio':anuncio,
                                         'categoria':categoria})
 
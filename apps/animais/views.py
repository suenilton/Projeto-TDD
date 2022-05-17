from django.shortcuts import render, redirect
from .models import Animais

def index(request):
    caracteristicas = None

    if 'buscar' in request.GET:
        animais = Animais.objects.all()
        animal_pesquisado = request.GET['buscar']
        caracteristicas = animais.filter(nome_animal__icontains=animal_pesquisado)

    context = {'caracteristicas':caracteristicas}

    return render(request, 'index.html', context)

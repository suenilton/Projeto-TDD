from django.shortcuts import render, redirect
from .models import Animais
from django.contrib import messages

def index(request):
    caracteristicas = None

    if 'buscar' in request.GET:
        animais = Animais.objects.all()
        animal_pesquisado = request.GET['buscar']
        if animal_pesquisado == '':
            caracteristicas = None
        else:
            caracteristicas = animais.filter(nome_animal__icontains=animal_pesquisado)
            if not caracteristicas:
                messages.error(request, 'Animal pesquisado não encontrado.')

    context = {'caracteristicas':caracteristicas}

    return render(request, 'index.html', context)

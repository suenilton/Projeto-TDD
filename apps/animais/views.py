from django.shortcuts import render, redirect
from .models import Animais

def index(request):
    caracteristicas = Animais.objects.all()

    context = {'caracteristicas':caracteristicas}

    return render(request, 'index.html', context)

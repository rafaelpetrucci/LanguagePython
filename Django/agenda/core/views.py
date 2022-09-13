from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.


def home(requests):
    return HttpResponse("<h1>Bem vindo!</h1>")


def titulo(requests, titulo_evento):
    total = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('{}'.format(total))
from django.shortcuts import render
from .models import Agenda

# Create your views here.

def home(request):
    agenda = Agenda.objects.all()
    return render(request, 'pages/home.html', {'agenda': agenda})

def agenda_detalhe(request, id):
    agenda = Agenda.objects.get(id=id)
    return render(request, 'pages/agenda_detalhe.html', {'agenda': agenda})

def lista_contatos(request):
    contatos = Agenda.objects.all()
    return render(request, 'pages/lista_contatos.html', {'contatos': contatos})
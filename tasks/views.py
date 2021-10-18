from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

# Função que conotrola a apresentação da view tasks/list.html

def index(request):
  tasks = Task.objects.all() # pega todos os objetos tasks

  context =  {'tasks': tasks} # Coloca tasks em um dicionário para poder renderizar na view
  return render(request, 'tasks/list.html', context) # context como um terceiro parâmetro para poder renderizar na view
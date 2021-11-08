from django.db import reset_queries
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

# Função que controla a apresentação do HTML tasks/list.html

def index(request):
  tasks = Task.objects.all() # pega todos os objetos tasks
  form = TaskForm()

# Fazer as tasks aparecerem na view
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('/')

  context =  {'tasks': tasks, 'form': form} # Coloca tasks em um dicionário e em uma variável para poder renderizar na view
  return render(request, 'tasks/list.html', context) # renderiza a view tasks/list.html com context como um terceiro parâmetro



def updateTask(request, pk):
  task = Task.objects.get(id=pk)

  form = TaskForm(instance=task)
  
  if request.method =='POST':
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('/')
    
  context = {'form':form}

  return render(request, 'tasks/update_task.html', context)



def deleteTask(request, pk):
  item = Task.objects.get(id=pk)

  if request.method == 'POST':
    item.delete()
    return redirect('/')

  context = {'item':item}

  return render(request, 'tasks/delete.html', context)
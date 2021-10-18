from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Task) # Cria campos automáticos no admin gerados através do model criado

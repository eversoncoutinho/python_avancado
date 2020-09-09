from django.contrib import admin

# Register your models here.
from .models import Categoria, Anuncio

admin.site.register(Categoria)
admin.site.register(Anuncio)


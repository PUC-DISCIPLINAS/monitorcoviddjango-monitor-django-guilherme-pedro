from django.contrib import admin
from .models import Dados


# Register your models here.
@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    list_display = ['id', 'pais','casos_confirmados', 'mortes', 'recuperados']

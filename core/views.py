from django.db import connections
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Dados

# Create your views here.

def login_user(request):
    return render(request, 'login.html')



def list_data(request):
    dados = {"casos": Dados.objects.all()}
    return render(request, 'index.html', dados)

@csrf_protect
def authenticate_login(request):
    if request.POST:
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Senha ou Usuário incorretos.')
        return redirect('/login')


def logout_user(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def register(request):
    return render(request, 'register.html')

@login_required(login_url='/login/')
def delete_dados(request):
    return render(request, 'delete.html')

@login_required(login_url='/login/')
def delete(request, id):
    dados = Dados.objects.get(id=id)
    dados.delete()
    return redirect('/list')

@login_required(login_url='/login/')
def set_dados(request):
    pais = request.POST.get('pais')
    mortes = request.POST.get('mortes')
    recuperados = request.POST.get('recuperados')
    casos_confirmados = int(mortes) + int(recuperados)
    caso_id = request.POST.get('caso_id')
    if caso_id:
        dados = Dados.objects.get(id=caso_id)
        if pais == dados.pais:
            dados.mortes = mortes
            dados.recuperados = recuperados
            dados.casos_confirmados = casos_confirmados 
            dados.save()
    else:
        dados = Dados.objects.create(pais=pais, mortes=mortes, recuperados=recuperados, casos_confirmados=casos_confirmados,)
    return redirect('/list/')


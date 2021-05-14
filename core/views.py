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
    dados = Dados.objects.all().values()
    for d in dados:
        print(d)
    return render(request, 'index.html',{dados: dados})

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
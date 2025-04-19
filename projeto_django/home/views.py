from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Quarto
from .forms import UserRegistrationForm, QuartoForm

def home_view(request):
    return render(request, 'home/home.html')

def quartos_view(request):
    rooms = Quarto.objects.all()
    return render(request, 'quartos/listagem_quartos.html', {'rooms': rooms})

def quartos_detalhes(request, quarto_id):
    quarto = get_object_or_404(Quarto, id=quarto_id)
    return render(request, 'quartos/quartos_detalhes.html', {'quarto': quarto})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'home/cadastrar.html', {'form': form})

def login_usuario(request):
    next_url = request.GET.get('next', 'home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            auth_login(request, user)
            return redirect(request.POST.get('next', next_url))
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos. Tente novamente.')
    
    return render(request, 'home/login.html', {'next': next_url})

@login_required
def logout_usuario(request):
    auth_logout(request)
    return redirect('home')

@login_required
def criar_quarto(request):
    if request.method == 'POST':
        form = QuartoForm(request.POST, request.FILES)
        if form.is_valid():
            novo_quarto = form.save(commit=False)
            novo_quarto.proprietario = request.user
            novo_quarto.save()
            messages.success(request, 'Quarto cadastrado com sucesso!')
            return redirect('quartos')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')
    else:
        form = QuartoForm()
    
    return render(request, 'quartos/criar_quarto.html', {'form': form})

@login_required
def meus_quartos(request):
    meus_quartos = Quarto.objects.filter(proprietario=request.user)
    return render(request, 'quartos/meus_quartos.html', {'rooms': meus_quartos})

@login_required
def editar_quarto(request, quarto_id):
    quarto = get_object_or_404(Quarto, id=quarto_id, proprietario=request.user)
    
    if request.method == 'POST':
        form = QuartoForm(request.POST, request.FILES, instance=quarto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quarto atualizado com sucesso!')
            return redirect('meus_quartos')
    else:
        form = QuartoForm(instance=quarto)
    
    return render(request, 'quartos/editar_quarto.html', {'form': form, 'quarto': quarto})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta
from django.utils import timezone
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import crearConsultaForm, responderConsultaForm
from django.conf import settings


def index(request):
    return render(request, 'drugs/index.html', {})

def infomarihuana(request):
    return render(request, 'drugs/infomarihuana.html', {})    

def consultas(request):
    Consultas = Consulta.objects.filter(respondida=True)
    return render(request, 'drugs/consultas.html', {"Consultas":Consultas})

def crearConsulta(request):
    if request.method == "POST":
        form = crearConsultaForm(request.POST)
        if form.is_valid():
            Consulta = form.save(commit=False)
            Consulta.nombre=request.user.username
            Consulta.email=request.user.email
            Consulta.respuesta=""
            Consulta.respondida = False
            Consulta.save()
            return redirect('consultas')
    else:
        form = crearConsultaForm()
    return render(request, 'drugs/crearConsulta.html', {"form":form})

def registrar(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('index')

        return render(request = request, template_name = 'drugs/registrarme.html', context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = 'drugs/registrarme.html',
                  context={"form":form})
                
def consultaResponder(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    pregunta = get_object_or_404(Consulta, pk=pk)
    if request.method == "POST":
        form = responderConsultaForm(request.POST, instance=pregunta)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.respondida = True
            consulta.save()
            return redirect('respPreguntas')
    else:
        form = responderConsultaForm(instance=pregunta)
    return render(request, 'sol/pregunta_responder.html', {'form':form,'consulta':consulta})

def consultaEliminar(request, pk):
    if not request.user.is_superuser:
        return redirect('consultas')
    consulta = get_object_or_404(Consulta, pk=pk)
    consulta.delete()
    return redirect('consultas')
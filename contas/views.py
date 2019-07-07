# Escreva as views aqui

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
import datetime
from .forms import TransacaoForm


def home(request):

    #Criando um dicionario de variaveis que será passada para o template
    now = datetime.datetime.now()
    data = {}
    data['now'] = now
    data['transacao'] = ['t1', 't2', 't3']

    #html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacao'] = Transacao.objects.all()

    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):

    #Cria um formulario
    form = TransacaoForm(request.POST or None)
    data = {}

    #Verifica se é valido para salvar, se for chama 'listagem'
    if form.is_valid():
        form.save()
        return redirect('url_listagem')       # Redirect, redireciona para a pagina sem duplicar os dados vindo do POST

    data['form'] = form

    return render(request, 'contas/form.html', data)


def update(request, pk):

        data = {}
        transacao = Transacao.objects.get(pk=pk)                        #Busca um objeto transacao filtrado pela PK
        form = TransacaoForm(request.POST or None, instance=transacao)      #Instancia um form com os dados da 'PK'

        if form.is_valid():
            form.save()
            return redirect('url_listagem')

        data['form'] = form
        data['transacao'] = transacao
        return render(request, 'contas/form.html', data)

def delete(request, pk):

    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()

    return redirect('url_listagem')

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services import Cidade

# recebe a requisição e retorna uma resposta
def index2(request):
    cidades = Cidade.lista()
    return render(request, "index2.html", {'cidades': cidades})


def previsao_view(request):
    nome_cidade = str(request.GET.get('cidade'))

    if not nome_cidade:
        return JsonResponse({'erro': 'Nome da cidade não informado.'})
    
    previsao = Cidade.cidade_encontrar(nome_cidade)

    if previsao is None:
        return JsonResponse({'erro': 'Cidade não cadastrada.'})
    
    return JsonResponse({
        'nome': nome_cidade, 
        'previsao': previsao
    })

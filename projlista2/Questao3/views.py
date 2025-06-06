from django.shortcuts import render
from django.http import JsonResponse
from .services import Capital, Frete
from django.template.loader import render_to_string

# Create your views here.
def index3(request):
    capitais = Capital.lista()
    return render(request, "index3.html", {'capitais': capitais})

def frete_view(request):
    origem = (request.GET.get('origem'))
    destino = (request.GET.get('destino'))

    frete_calculo = Frete.calculo(origem, destino)

    html = render_to_string("partials/tabela_frete.html", { #serve para renderizar um template em uma string 
        'origem': origem,
        'destino': destino,
        'frete': frete_calculo
    })

    return JsonResponse({
        'html': html
    })
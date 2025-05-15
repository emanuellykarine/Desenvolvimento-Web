#View serve para pegar uma requisição e retornar uma resposta

from django.shortcuts import render
#from django.http import HttpResponse

def index(request): #Função render de atalho para pegar o template html
    return render(request, 'index.html')

def calcular_imc(request): #Utilizando template html 
    altura = float(request.GET.get('altura')) #Na minha requisição do tipo GET pegue a altura
    peso = float(request.GET.get('peso'))
    imc= peso/(altura*altura)
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'
    contexto= { #Um dicionário que passa 4 informações 
        'imc': imc,
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso,
    }
    return render(request, 'resultado_imc.html', contexto) #renderizar o html

#index utilizando a escrita html na propria view com htttp response
# def index(request): #toda view que é implementada tem que ter o parametro request 
#     return HttpResponse("<h1> Bem-vindo(a) à aplicação IMC</h1>") #retorne uma resposta http 

# def calcular(request):
#     return HttpResponse("<h1> 2 + 2 = 4 </h1>")

#outra forma de calcular
# def calcular(request):
#     numero = 2
#     soma = numero+numero
#     return HttpResponse(f'<h1>{numero} + {numero} = {soma}</h1>')

#calculo  do imc inicial 
# def calculo_imc(request, altura, peso):
#     altura = altura / 100
#     response = f'Calculo do IMC: {peso/(altura*altura)}'
#     return HttpResponse(response)


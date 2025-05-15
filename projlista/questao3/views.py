from django.shortcuts import render

dias=["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
# Create your views here.
def index_questao3(request):
    contexto={'dias':dias}
    return render(request, 'index_questao3.html', contexto)

def resultado_questao3(request):
    dias_semana = request.GET.getlist('dias')
    temas = str(request.GET.get('temas'))
    temas_lista = temas.split(',')

    cronograma = {dia: [] for dia in dias_semana} #Cria um dicionário em que o valor vai ser a lista contendo os temas
    for i in range (len(temas_lista)): #vai até o fim da lista de temas pois todos tem que ser distribuidos
        dia = dias_semana[i % len(dias_semana)] #caso os dias sejam menores que a quantidade de temas faz o calculo pra voltar 
        cronograma[dia].append(temas_lista[i])

    contexto={'cronograma':cronograma}
    return render(request, 'resultado_questao3.html', contexto)



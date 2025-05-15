from django.shortcuts import render

# Create your views here.
def index_questao1(request):
    return render(request, 'index_questao1.html')

def resultado_questao1(request):
    consumo = int(request.GET.get('consumo'))
    if (consumo <= 100):
        resultado = consumo * 0.50
    elif (consumo <= 200):
        resultado = (100 * 0.50) + ((consumo - 100) * 0.75)
    else:
        resultado = (100 * 0.50) + (100 * 0.75) + ((consumo - 200) * 1.00)
    
    resultado_final={
        'resultado':resultado
    }
    return render(request, 'resultado_questao1.html', resultado_final)
from django.shortcuts import render
from . import services

# Create your views here.
def index_enquete(request):
    return render(request, 'index_enquete.html')

def resultados_view(request):
    genero = str(request.POST.get('genero'))
    
    valores=services.resultados(genero)
   
    return render(request, 'resultado_generos.html', valores)
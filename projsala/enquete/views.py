from django.shortcuts import render

cont_terror = 0
cont_acao = 0
cont_drama = 0
cont_comedia = 0

# Create your views here.
def index_enquete(request):
    return render(request, 'index_enquete.html')

def resultados(request):
    genero = str(request.GET.get('genero'))
    if (genero == "Ação"):
        global cont_acao
        cont_acao += 1
    elif (genero == "Terror"):
        global cont_terror
        cont_terror += 1
    elif (genero == "Comédia"):
        global cont_comedia
        cont_comedia += 1
    elif (genero == "Drama"):
        global cont_drama
        cont_drama += 1
    
    valores={
        'acao': cont_acao,
        'comedia': cont_comedia,
        'drama': cont_drama,
        'terror': cont_terror
    }
    return render(request, 'resultado_generos.html', valores)
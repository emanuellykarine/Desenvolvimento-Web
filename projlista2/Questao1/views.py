from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services import Postagem, Comentario

postagens = [
    Postagem("Django", "Django é um framework web e alto nível e código aberto, escrito em Python, projetado para o desenvolvimento rápido, seguro e escalável."),
    Postagem("JavaScript", "JavaScript (JS) é uma linguagem de programação que, em essência, permite que sites e aplicações web interajam com o utilizador e com o servidor, tornando a experiência mais dinâmica e interativa.")
]

def index(request):
    return render(request, "index.html", {'postagens': postagens})


def lista_comentarios_view(request):
    if request.method == 'GET': #Se está apenas pedindo dados, método GET
        return redirect('imc:index') #Redireciona para a URL index
    
    index_post = int(request.POST.get('post_index')) 
    conteudo = str(request.POST.get('conteudo'))
    autor = str(request.POST.get('autor'))
    
    comentario = Comentario(conteudo, autor)
    postagens[index_post].lista_comentarios(comentario)

    return JsonResponse({
        'autor': autor,
        'conteudo': conteudo
    })

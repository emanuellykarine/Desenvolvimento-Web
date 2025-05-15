from django.shortcuts import render

# Create your views here.
def index_questao2(request):
    return render(request, 'index_questao2.html')

def resultado_questao2(request):
    valor_emprestimo = float(request.GET.get('valor_emprestimo'))
    taxa = int(request.GET.get('taxa'))
    n_parcelas = int(request.GET.get('n_parcelas'))

    montante = valor_emprestimo * (1 + (taxa/100)) ** n_parcelas
    parcela = montante / n_parcelas

    resultado = {
        'valor_emprestimo': valor_emprestimo,
        'taxa': taxa,
        'n_parcelas': n_parcelas,
        'montante':round(montante, 2),
        'parcela':round(parcela, 2)
    }

    return render(request, 'resultado_questao2.html', resultado)
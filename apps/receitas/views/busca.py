from django.shortcuts import get_object_or_404, render, redirect
from receitas.models import Receita

def buscar(request):
    """Busca receitas no sistema filtrando por nome """
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_buscar)

    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'receitas/buscar.html', dados)
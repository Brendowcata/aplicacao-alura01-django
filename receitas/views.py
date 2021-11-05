from django.shortcuts import render

def index(request):

    receitas = {
        1:'Lasanha',
        2:'Pizza',
        3:'Sopa de legumes',
        4:'Sorvete',
        5:'Macarrão',
        6:"Molho de salsicha"
    }

    dados = {
        'nome_das_receitas' : receitas
    }
    return render(request,'index.html', dados)

def receita(request):
    return render(request,'receita.html')


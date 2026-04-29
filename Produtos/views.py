from django.shortcuts import render

def home_produtos(request):
    return render(request , 'Produtos/home_produtos.html')
# Create your views here.

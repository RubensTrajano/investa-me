from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm

#def pagina_inicial(request):
 #   return HttpResponse('Pronto para Investir')

def contato(request):
    return HttpResponse('Para duvidadas, enviar e-mail para jose')
    
def minha_historia(request):
    pessoas = {
        'nome': 'Jeff',
        'idade': '26',
        'hobby': 'namora'
    }
    return render(request,'investimentos/minha_historias.html', pessoas)

#def novo_investimentos(request):
 #   return render(request, 'investimentos/novo_investimentos.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento'),
    }
    return render(request, 'investimentos/investimento_registrado.html',investimento)



def investimentos(request):
    dados = {
        'dados':Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)
    
#def novo_investimentos(request):
#    return render(request, 'investimentos/novo_investimentos.html')

def datalhe(request, id_investimento):
  dados = {
     'dados': Investimento.objects.get(pk=id_investimento)

  }  
  return render(request, 'investimentos/detalhe.html', dados)

#criar dados aparti da web
def criar(request):    

    if request.method == 'POST':

        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
             investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimentos.html', context=formulario)
#editar dados
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
       formulario = InvestimentoForm(instance=investimento)
       return render(request,'investimentos/novo_investimentos.html',{'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

#excluir dados criado

def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html',{'item': investimento })
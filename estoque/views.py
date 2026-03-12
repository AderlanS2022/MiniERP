from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MovimentacaoEstoque
from .forms import MovimentacaoEstoqueForm
from produtos.models import Produto


def lista_movimentacoes(request):

    movimentacoes = MovimentacaoEstoque.objects.select_related('produto').all().order_by('-data')

    context = {
        'movimentacoes': movimentacoes
    }

    return render(request, 'estoque/lista.html', context)


def nova_movimentacao(request):

    form = MovimentacaoEstoqueForm(request.POST or None)

    if form.is_valid():

        movimentacao = form.save(commit=False)
        movimentacao.usuario = request.user
        movimentacao.save()

        produto = movimentacao.produto

        if movimentacao.tipo == 'E':
            produto.estoque += movimentacao.quantidade

        elif movimentacao.tipo == 'S':
            produto.estoque -= movimentacao.quantidade

        elif movimentacao.tipo == 'A':
            produto.estoque = movimentacao.quantidade

        produto.save()

        messages.success(request, "Movimentação registrada com sucesso!")
        return redirect('lista_movimentacoes')

    context = {
        'form': form
    }

    return render(request, 'estoque/movimento.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm


def lista_produtos(request):

    produtos = Produto.objects.all()

    return render(request, 'produtos/lista.html', {
        'produtos': produtos
    })


def criar_produto(request):

    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'produtos/form.html', {
        'form': form,
        'titulo': 'Novo Produto'
    })


def editar_produto(request, id):

    produto = get_object_or_404(Produto, id=id)

    form = ProdutoForm(
        request.POST or None,
        request.FILES or None,
        instance=produto
    )

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'produtos/form.html', {
        'form': form,
        'titulo': 'Editar Produto'
    })


def excluir_produto(request, id):

    produto = get_object_or_404(Produto, id=id)
    produto.delete()

    return redirect('lista_produtos')

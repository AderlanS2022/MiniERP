from decimal import Decimal, InvalidOperation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

# Se você já tem model Caixa no pdv/models.py, mantenha e ajuste os imports.
# Abaixo vai um modelo simples esperado:
from .models import Caixa


@login_required
def pdv_home(request):
    caixa_id = request.session.get("caixa_id")
    if not caixa_id:
        return redirect("pdv:abrir_caixa")

    # valida se ainda está aberto
    if not Caixa.objects.filter(id=caixa_id, aberto=True).exists():
        request.session.pop("caixa_id", None)
        return redirect("pdv:abrir_caixa")

    return redirect("pdv:caixa")


@login_required
def abrir_caixa(request):
    # Se já tem caixa aberto na sessão, manda direto pro PDV
    caixa_id = request.session.get("caixa_id")
    if caixa_id and Caixa.objects.filter(id=caixa_id, aberto=True).exists():
        return redirect("pdv:caixa")

    if request.method == "POST":
        valor_inicial_raw = (request.POST.get("valor_inicial") or "").replace(",", ".").strip()

        try:
            valor_inicial = Decimal(valor_inicial_raw) if valor_inicial_raw else Decimal("0.00")
            if valor_inicial < 0:
                raise InvalidOperation
        except (InvalidOperation, ValueError):
            messages.error(request, "Valor inicial inválido. Ex: 50,00")
            return render(request, "pdv/abrir_caixa.html")

        caixa = Caixa.objects.create(
            operador=request.user,
            aberto=True,
            abertura_em=timezone.now(),
            valor_inicial=valor_inicial,
        )
        request.session["caixa_id"] = caixa.id
        messages.success(request, "Caixa aberto com sucesso!")
        return redirect("pdv:caixa")

    return render(request, "pdv/abrir_caixa.html")


@login_required
def caixa_fullscreen(request):
    caixa_id = request.session.get("caixa_id")
    if not caixa_id:
        return redirect("pdv:abrir_caixa")

    caixa = Caixa.objects.filter(id=caixa_id, aberto=True).first()
    if not caixa:
        request.session.pop("caixa_id", None)
        return redirect("pdv:abrir_caixa")

    # ✅ Aqui é apenas front-end bonito por enquanto.
    # Depois a gente pluga com banco (itens da venda, busca por código de barras, etc).
    itens_demo = [
        {"nome": "Coca-Cola 350ml", "codigo": "7891100000016", "preco": "5,00", "qtd": 5, "icone": "bi-cup-straw"},
        {"nome": "Desodorante XYZ 90g", "codigo": "7991120002225", "preco": "12,00", "qtd": 2, "icone": "bi-droplet"},
        {"nome": "Arroz Branco 1kg", "codigo": "7991131133005", "preco": "8,00", "qtd": 1, "icone": "bi-bag"},
        {"nome": "Detergente Alfa 500ml", "codigo": "7891140044445", "preco": "2,50", "qtd": 3, "icone": "bi-bucket"},
        {"nome": "Chocolate ABC 100g", "codigo": "799115006778", "preco": "6,00", "qtd": 1, "icone": "bi-square-fill"},
    ]

    context = {
        "caixa": caixa,
        "itens": itens_demo,
        "subtotal": "32,00",
        "desconto": "0,00",
        "total": "32,00",
    }
    return render(request, "pdv/caixa_fullscreen.html", context)


@login_required
def fechar_caixa(request):
    caixa_id = request.session.get("caixa_id")
    if not caixa_id:
        return redirect("pdv:abrir_caixa")

    caixa = Caixa.objects.filter(id=caixa_id, aberto=True).first()
    if caixa:
        caixa.aberto = False
        caixa.fechamento_em = timezone.now()
        caixa.save(update_fields=["aberto", "fechamento_em"])

    request.session.pop("caixa_id", None)
    messages.success(request, "Caixa fechado.")
    return redirect("pdv:abrir_caixa")
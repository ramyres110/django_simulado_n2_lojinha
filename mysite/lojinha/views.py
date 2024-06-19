from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

from . import models

# Create your views here.
def page_inicio(request):
    produtos = models.Produto.objects.all()
    return render(request, "inicio.html", {"produtos": produtos})

def page_produto_detalhe(request, produto_id):
    produto = get_object_or_404(models.Produto, id=produto_id)
    return render(request, "produto.html", {"produto": produto})

def page_promocao(request):
    promocoes = models.Promocao.objects.all()
    return render(request, "promocoes.html", {"promocoes": promocoes})

def page_contato(request):
    if request.method == 'POST':
        nome = request.POST["nome"]
        email = request.POST["email"]
        mensagem = request.POST["mensagem"]
        contato = models.Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
        contato.save()
        return redirect("inicio")
    else:
        return render(request, "contato.html", {})
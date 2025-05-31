from flask import Blueprint, render_template, redirect
from apimercadopago import criar_link_pagamento
from conexao import conectar

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT id, nome_produto, preco, estoque FROM apimercadopago")
    produtos = cur.fetchall()

    
    return render_template("homepage.html", produtos=produtos)

@main.route("/comprar/<produto_id>")
def comprar(produto_id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute('''
        SELECT id, nome_produto, preco, estoque 
        FROM apimercadopago
        WHERE id = %s
                          ''', (produto_id,))
    produto = cur.fetchone()

    
  
    if not produto:
        return "Produto não encontrado", 404
    

    product_list = {
        "id":produto[0],
        "title":produto[1],
        "quantity":1,
        "unit_price":float(produto[2]),

    }

    link = criar_link_pagamento(product_list)
    if link:
        return redirect(link)
        
    else:
        return "Erro ao criar link de pagamento", 500

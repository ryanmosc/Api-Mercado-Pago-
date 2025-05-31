#Baixe a api do mercado pago (pip install mercadopago)
#Se quiser ver o Json melhor baixe o pprint


#importe os conectores
import mercadopago
import pprint

#Uso o metodo sdk por ser mais simples, mas tem outro~
#Passo a chave de api (Mesmo esquema da outra api)
sdk = mercadopago.SDK("Seu token de api")


#Configs da Api que sao obrigatorias 
request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
}


#Na documentação ela exige que seja passado os parametros desse jeito mas existem outras que nao quis colocar, essas sõa as principais e umas são obrigatorias
payment_data = {
    "items":[
        #Se quiser integrar com um banco de dados, aqui é a hora, no final coloco um exemplo
        {"id": "1", 
        "title": "Camisa Regata Linda",
        "quantity": 1,
        "currency_id": "BRL",
        "unit_price": 200
        
        
        }
    ],

    #Urls de volta apos o pagemento 
    "back_urls": {
    "success": "https://test.com//compracerta",
    "pending": "https://test.com/pending",
    "failure": "https://test.com/compraerrada",
    },

    #Sempre retornar para um template 
    "auto_return": "all"

    
}

#Manipulando O json

#Um ponto de observação é que como estou usando a biblioteca sdk, a preferencia é SDK

#A variavel result cria o json com todos os dados do boleto , inclusive o link que pode ser integrado com um botao "Comprar"
result = sdk.preference().create(payment_data, request_options)

#payment é responsavel pelo oq importa para fazer o boleto
payment = result["response"]


#Aqui usei regras de retorno da internet para se caso der certo a conexao da API,  ele  pega do json o link e me retorna, no caso printando no terminal
if result["status"] == 201:
    #Response == Aonde esta os dados do json init_point == nome da varivel que tem o link no Json
    init_point = result["response"]["init_point"]
    print(init_point)

# pprint.pprint(payment)
# print(payment)



#----------------------------------------------------EXEMPLO DE CODIGO COM BANCO-----------------------------------------------------------------#                                                                 #  #


# def comprar(produto_id):
#     conn = conectar()
#     cur = conn.cursor()

#     cur.execute('''
#         SELECT id, nome_produto, preco, estoque 
#         FROM apimercadopago
#         WHERE id = %s
#                           ''', (produto_id,))
#     produto = cur.fetchone()

    
  
#     if not produto:
#         return "Produto não encontrado", 404
    

#     product_list = {
#         "id":produto[0],
#         "title":produto[1],
#         "quantity":1,
#         "unit_price":float(produto[2]),

#     }

#     link = criar_link_pagamento(product_list)
#     if link:
#         return redirect(link)
        
#     else:
#         return "Erro ao criar link de pagamento", 500

import mercadopago
import uuid

sdk = mercadopago.SDK("APP_USR-1908395326154010-052818-074803d7349bd31e8866d8ca7a7d1fb6-2462681687")

def criar_link_pagamento(product_list):
    payment_data = {
        "items": [
            {
                "id": product_list["id"],
                "title": product_list["title"],
                "quantity": product_list["quantity"],
                "currency_id": "BRL",
                "unit_price": product_list["unit_price"]
            }
        ],
        "back_urls": {
            "success": "https://test.com/compracerta",
            "pending": "https://test.com/pending",
            "failure": "https://test.com/compraerrada"
        },
        "auto_return": "all"
    }

    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
        'x-idempotency-key': str(uuid.uuid4())
    }

    result = sdk.preference().create(payment_data, request_options)
    if result["status"] == 201:
        init_point = result["response"]["init_point"]
        print(init_point)
        
        return result["response"]["init_point"]
    else:
        return None

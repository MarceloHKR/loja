


clientes = {
    "Gabriel":{
        'loja': 'RPGStore',
        'cidade': 'Laranjeiras do Sul',
        'pedido': " Dados de 20 lados"
    }


}


import json

with open('pedidos.json', 'w', encoding='utf-8') as f:
    json.dump(clientes, f, ident=4, ensure_ascii=False)
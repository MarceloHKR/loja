import json

clientes = json.load(open('pedidos.json', 'r', encoding='utf-8'))

while True:
    print('Digite a opção desejada:')
    print('1 - Fazer um Pedido')
    print('2 - Cancelar Pedido')
    print('3 - Sair')

    input_opcao = input('Opção: ')

    if input_opcao == '1':
        input_cliente = input('Digite seu nome: ')
        if clientes.get(input_cliente, False):
            print("Pedido já registrado")
            continue
        input_loja = input('Digite o nome da Loja: ')
        input_cidade = input('Digite o nome da cidade: ')
        input_pedido = input('Digite o nome do profuto: ')

        clientes[input_cliente] = {
            'loja': input_loja,
            'cidade': input_cidade,
            'pedido': input_pedido
        }

        json.dump(
            clientes,
            open('pedidos.json', 'w', encoding='utf-8'),
            indent=4,
            ensure_ascii=False
        )

    #buscar cliente
    if input_opcao == '2':
        input_cliente = input('Digite o seu nome: ')
        dados_cliente = clientes.get(input_cliente, False)
        if dados_cliente:
            print('Dados do Cliente:', input_cliente)
            print(dados_cliente)
        else:
            print('Cliente não encontrado!')

    #sair do programa
    if input_opcao == '3':
        break
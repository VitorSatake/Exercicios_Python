"""
Projeto 2 - Mercado

Descrição:

Devemos desenvolver uma aplicação onde ao ser inicializada apresente ao usuário um menu onde seja possível
cadastrar, listar e comprar produtos, além de visualizar o carrinho de compra ou sair da aplicação.

Ao adicionar um produto no carrinho de compras, deve-se verificar se ja existe um mesmo produto no carrinho,
bastando alterar a quantidade.

Ao finalizar a compra deve ser apresentado ao usuário o total de acordo com os produtos e quantidades 
inseridas no carrinho de compra.

"""

from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('======================================')
    print('============ Bem Vindo(a) ============')
    print('========== Mercado Python ============')
    print('======================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(1)
        exit(0)
    else:
        print('Opção Inválida!')
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('====================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = input('Informe o preço do produto: ')

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('-------------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados!')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('------------------------------------------------')
        print('============ Produtos Disponíveis ==============')
        for produto in produtos:
            print(produto)
            print('--------------------------------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                sleep(2)
                menu()
        else:
            print(f"O produto com o código {codigo} não foi encontrado.")
            sleep(2)
            menu()
    else:
        print(f'Ainda não existem produtos para vender.')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no Carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('---------------------------------')
                sleep(1)
    else:
        print(f'Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-----------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho!')
    sleep(2)
    menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
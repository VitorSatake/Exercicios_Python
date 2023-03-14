"""
Projeto 3 - Banco

Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o que deseja fazer no banco, 
como criar uma conta, efetuar saque, efetuar depósitoefetuar transferência , listar contas ou sair do sistema.

"""

from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    pass

def criar_conta() -> None:
    pass

def efetuar_saque() -> None:
    pass

def efetuar_deposito() -> None:
    pass

def efetuar_transferencia() -> None:
    pass

def listar_contas() ->None:
    pass

def buscar_conta_por_numero(numero: int) -> Conta:
    pass

if __name__ == '__main__':
    main()
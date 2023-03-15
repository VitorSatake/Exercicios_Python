"""
Projeto 1 - Game

Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o nível de
dificuldade do jogo e após isso gere e apresenta, de forma aleatória, um cálculo para que possamos 
informar o resultado.

Iremos limitar as opções em somar, subtrair e multiplicar.

Se o usuário acertar a resposta, somará 1 ponto ao seu score.

Acertando ou errando, ele poderá ou não continuar o jogo.

"""

from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Iforme o nível de dificuldade desejado [1, 2, 3, ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()
    
    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo ? [1 - sim, 0 - não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
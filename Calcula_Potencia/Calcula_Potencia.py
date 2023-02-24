N = input("Digite o número a ser potenciado: ")
N = int(N)

P = input("Digite a potência desejada: ")
P = int(P)

while((P < 0) or (N <= 1)):
    print("Entrada inválida!")
    N = input("Digite o número a ser potenciado: ")
    N = int(N)

    P = input("Digite a potência desejada: ")
    P = int(P)

Pote = 1
if P > 0:
    for j in range(1,P + 1):
        Pote = Pote * N

print()        
print(N,"elevado a", P, ":", Pote)
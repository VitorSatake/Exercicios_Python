import os  # importa o módulo do sistema operacional

os.system("cls") or None #limpa a tela antes de iniciar o código quando for rodar

# Entrada de dados

num1 = input("Digite o primeiro número: ")
num1 = int(num1)  # converte num de string para valor numérico

num2 = input("Digite o segundo número: ")
num2 = int(num2)  # converte num de string para valor numérico

# Processamento

mult = num1 * num2

# Saída da informação

print()
print("A multiplicação de", num1, "por", num2, "é", mult) 
from models.cliente import Cliente
from models.conta import Conta


felicia: Cliente = Cliente('Felicia', 'felicia@gmail.com', '123.456.789-00', '02/09/1987')
angela: Cliente = Cliente('Angela', 'angela@gmail.com', '987.456.789-02', '08/07/1978')

#print(felicia)

contaf: Conta = Conta(felicia)
contaa: Conta = Conta(angela)

print(contaf)
print(contaa)
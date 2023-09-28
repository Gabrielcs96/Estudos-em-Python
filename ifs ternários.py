#If ternário
saldo= 1000
saque = 100

status= "sucesso" if saldo>=saque else "falha"

print(f"{status} ao realizar o saque!")